#!/usr/bin/env python
__author__ = "Pranat Dayal, Jimmy Hickey, Ian Stubenbord"

import pyshark
import sys
#import subprocess
import os

def cleanup():
	os.system("rm osmap.silk; rm osmap.yaf")
	

def generate(pcap):
	i = "rwp2yaf2silk --in=" + pcap + " --out=osmap.silk"
	j = "yaf --in " + pcap + " --out osmap.yaf"
	#subprocess.call(["yaf", i, "--out osmap.yaf"])
	os.system(i)
	os.system(j)

def analysis(cap):
	#this is where we can use pyshark to go through the capture 
	#provided and see what is in it
	return 0

def main():
	#print out usage message if file not provided or too many args
	if len(sys.argv) != 2:
		print "Usage: osmap <pcap file>"
	#open up provided file in pyshark and do analysis
	else:
		pcap = sys.argv[1]
		cap = pyshark.FileCapture(sys.argv[1])
		analysis(cap)
		generate(pcap)
		cleanup()

if __name__=="__main__": main()
