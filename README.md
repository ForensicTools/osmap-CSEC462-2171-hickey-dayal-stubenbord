# osmap project (MIT License)
# Authors: Pranat Dayal, Jimmy Hickey, Ian Stubenbord 

DESCRIPTION:
-----------
OSmap is a network visualization tool that performs passive OS discovery for hosts present in a given network traffic capture.  

OSmap is dependant on the p0f v3 for os detection. For osmap to run, p0f needs to be downloaded and built in the osmap directory. A copy of p0f is downloaded and installed with the configuration script. More information can be found at http://lcamtuf.coredump.cx/p0f3/. It can also be downloaded at the URL. Credit to Michal Zalewski and other developers of the tool. 

OSmap was made and configured to be run on Debian systems. Modification of the configuration file, or manual installation of the necessary files, may allow the program to run on other linux or unix systems.

INSTALLATION:
------------
    
    sudo ./configure.sh 

    ./osmap.py <pcap file> 




Authors: 

Pranat Dayal    pxd5104@rit.edu

Jimmy Hickey    jjh6308@rit.edu

Ian Stubenbord    ixs6256@rit.edu
