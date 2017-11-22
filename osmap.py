#!/usr/bin/env python
__author__ = "Pranat Dayal, Jimmy Hickey, Ian Stubenbord"

import pyshark
import sys
import os
import csv
import re

ip2os = dict()  # ip key -> Operating system Entry ['192.168.1.1': 'windows 10']

counts = dict()  # ip key -> # of lines IP seen in .p0f ['192.168.1.1': 142]
#def cleanup():
	#remove the files that were created in the running of the program
	#os.system("rm osmap.silk; rm osmap.yaf; rm osmap.p0f")
#	os.system("rm osmap.silk; rm osmap.yaf")


def generate(pcap):
	#make a yaf file, a silk file, and make a file from p0f
#	i = "rwp2yaf2silk --in=" + pcap + " --out=osmap.silk"
#	j = "yaf --in " + pcap + " --out osmap.yaf"
	k = "./p0f -r ../" + pcap + " -o ../osmap.p0f > /dev/null"
	#subprocess.call(["yaf", i, "--out osmap.yaf"])
#	os.system(i)
#	os.system(j)
	os.chdir("p0f-JSON")
	os.system(k)
	os.chdir("..")

def analysis():
	#this is where we can use pyshark to go through the capture
	#provided and see what is in it
	#now lets use p0f to go through the lines and get the OS detected
	readFile = open("osmap.p0f", "r")
	for line in readFile:

		viable = re.search(r'(subj=...\|os=)', line)
		if viable:
			type = viable.group(1)[5:8]
			if type == 'cli':
				ip = re.search(r'(?<=cli=)(.*?)(?=\/)', line).group(1)
				os = re.search(r'(?<=os=)(.*?)(?=\|)', line).group(1)
			elif type == 'srv':
				ip = re.search(r'(?<=srv=)(.*?)(?=\/)', line).group(1)
				os = re.search(r'(?<=os=)(.*?)(?=\|)', line).group(1)

			counts[ip] = counts.get(ip, 0) + 1		# counts [ '192.0.0.1' : # of packets ]
			if ip not in ip2os:
				ip2os[ip] = os

def main():
	#print out usage message if file not provided or too many args
	if len(sys.argv) != 2:
		print "Usage: osmap <pcap file>"
	#open up provided file, create new files and do analysis, then cleanup
	else:
		pcap = sys.argv[1]
		cap = pyshark.FileCapture(sys.argv[1])
		generate(pcap)
		analysis()
		output = "osmap" + ".csv"
		with open(output,'wb') as csvfile:	  # create output csv using input file name
			outputWriter = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
			outputWriter.writerow(['title','category','views']) # 'IP','OS','# of Packets'
			for ip in counts:
				#print("IP: " + ip + "Tally:" + counts[ip] + "OS: " + ip2os[ip])
				outputWriter.writerow([ip,ip2os[ip],counts[ip]])
#		cleanup()

if __name__=="__main__": main()
