#!/usr/bin/env python
__author__ = "Pranat Dayal, Jimmy Hickey, Ian Stubenbord"

import pyshark
import sys
import os

#dictionary mapping ip to os, not including ??? values
ip2os = {}
#dictionary mapping ip to os, including ??? values
os_total = {}

def cleanup():
	#remove the files that were created in the running of the program
	#os.system("rm osmap.silk; rm osmap.yaf; rm osmap.p0f")
	os.system("rm osmap.silk; rm osmap.yaf")


def generate(pcap):
	#make a yaf file, a silk file, and make a file from p0f
	i = "rwp2yaf2silk --in=" + pcap + " --out=osmap.silk"
	j = "yaf --in " + pcap + " --out osmap.yaf"
	k = "./p0f -r ../" + pcap + " -o ../osmap.p0f > /dev/null"
	#subprocess.call(["yaf", i, "--out osmap.yaf"])
	os.system(i)
	os.system(j)
	os.chdir("p0f-JSON")
	os.system(k)
	os.chdir("..")

def analysis():
	#this is where we can use pyshark to go through the capture
	#provided and see what is in it
	#now lets use p0f to go through the lines and get the OS detected
	readFile = open("osmap.p0f", "r")
	for line in readFile:
		ip = getIP(line)
		os = getOs(line)
		if not (ip in ip2os) and (os == "???"):
			ip2os[ip] = os
		if not (ip in os_total):
			os_total[ip] = os
		if (ip in os_total) and (os == "???"):
			os_total[ip] = os

def getIP(line):
	#gets the IP address from the p0f output
	index = line.find("cli=")
	if index != -1:
		ipInfo = line[index:]
		split = ipInfo.partition("/")
		ip = split[0]
		return ip[4:]

def getOs(line):
	#this is where we can use regex to get the os detected from p0f
	#splitter = line.split();
	#data = splitter[2]
	#fields = data.split("|")
	#for i in fields:
	#	if i[0:3] == "os":
	#		print i
	index = line.find("os=")
	if index != -1:
		osInfo = line[index:]
		split = osInfo.partition("|")
		os = split[0]
		return os[3:]

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
		cleanup()

if __name__=="__main__": main()
