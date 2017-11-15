# osmap project (MIT License)
# Authors: Pranat Dayal, Jimmy Hickey, Ian Stubenbord 

OSmap is a network visualization tool that performs passive OS discovery for hosts present in a given network traffic capture.  

OSmap depends on using the pyshark python module, which is a python wrapper for tshark that allows the parsing of packets. The documentation and source code for pyshark can be found at https://github.com/KimiNewt/pyshark. Credit to KimiNewt.

OSmap is also dependant on the p0f v3 for os detection. For osmap to run, p0f needs to be downloaded and built in the osmap directory. A copy of p0f tar is included in the directory. More information can be found at http://lcamtuf.coredump.cx/p0f3/. It can also be downloaded at the URL. Credit to Michal Zalewski and other developers of the tool. 
