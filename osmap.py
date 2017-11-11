#!/usr/bin/env python
__author__ = "Pranat Dayal, Jimmy Hickey, Ian Stubenbord"

import pyshark
import sys
import os

def cleanup():
	#remove the files that were created in the running of the program
	os.system("rm osmap.silk; rm osmap.yaf; rm osmap.p0f")
	

def generate(pcap):
	#make a yaf file, a silk file, and make a file from p0f
	i = "rwp2yaf2silk --in=" + pcap + " --out=osmap.silk"
	j = "yaf --in " + pcap + " --out osmap.yaf"
	k = "./p0f -r ../" + pcap + " -o ../osmap.p0f > /dev/null"
	#subprocess.call(["yaf", i, "--out osmap.yaf"])
	os.system(i)
	os.system(j)
	os.chdir("p0f-3.09b")
	os.system(k)
	os.chdir("..")

def analysis():
	#this is where we can use pyshark to go through the capture 
	#provided and see what is in it
	#now lets use p0f to go through the lines and get the OS detected
	readFile = open("osmap.p0f", "r")
	for line in readFile:
		getOs(line)

def getOs(line):
	#this is where we can use regex to get the os detected from the line

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
