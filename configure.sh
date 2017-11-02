#!/bin/bash
#Configuration file
#to install YAF and SiLK
#for netflow analysis
#must run with sudo

red='\033[0;31m'
green='\033[0;32m'
nc='\033[0m'

function packages
{
    echo "${green}[*] Installing libglib2.0${nc}"
    apt-get -y install libglib2.0-dev
    echo "${green}[*] Installing libpcap${nc}"
    apt-get -y intall libpcap-dev
    echo "${green}[*] Installing python-dev${nc}"
    apt-get -y install python-dev
}

function downloads
{
    cd ~/tmp
    wget http://tools.netsa.cert.org/releases/silk-3.11.0.tar.gz
    wget http://tools.netsa.cert.org/releases/libfixbuf-1.7.0.tar.gz
    wget http://tools.netsa.cert.org/releases/yaf-2.7.1.tar.gz
}

function fixbuf
{
    cd ~/tmp
    tar -zxvf libfixbuf-1.7.0.tar.gz
    cd libfixbuf-1.7.0
    ./configure && make && make install
}

function yaf
{
    cd ~/tmp
    tar -zxvf yaf-2.7.1.tar.gz
    cd yaf-2.7.1
    export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
    ./configure --enable-applabel
    make
    make install
}

function silk
{
    cd ~/tmp
    tar -xvzf silk-3.11.0.tar.gz
    cd silk-3.11.0
    ./configure \
        --with-libfixbuf=/usr/local/lib/pkgconfig/ --with-python
    make
    make install
}

function main
{
    echo "${green}[*] Configuring OSmap${nc}"
    echo "${green}  Installing required packages${nc}"
    $(packages)
    echo "${green}[+] Completed installation of required packages${nc}"


}
main

