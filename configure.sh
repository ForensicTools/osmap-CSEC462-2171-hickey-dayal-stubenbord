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
    echo -e "${green} Installing required packages${nc}"
    echo -e "${green}[*] Installing libglib2.0${nc}"
    apt-get install libglib2.0-dev
    echo -e "${green}[*] Installing libpcap${nc}"
    apt-get install libpcap-dev
    echo -e "${green}[*] Installing python-dev${nc}"
    apt-get install python-dev
    echo -e "${green} [+] Completed installation of required packages${nc}"

}

function downloads
{
    wget http://tools.netsa.cert.org/releases/silk-3.11.0.tar.gz
    wget http://tools.netsa.cert.org/releases/libfixbuf-1.7.0.tar.gz
    wget http://tools.netsa.cert.org/releases/yaf-2.7.1.tar.gz
}

function fixbuf
{
    tar -zxvf libfixbuf-1.7.0.tar.gz
    cd libfixbuf-1.7.0
    ./configure && make && make install
}

function yaf
{
    tar -zxvf yaf-2.7.1.tar.gz
    cd yaf-2.7.1
    export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
    ./configure --enable-applabel
    make
    make install
}

function silk
{
    tar -xvzf silk-3.11.0.tar.gz
    cd silk-3.11.0
    ./configure \
        --with-libfixbuf=/usr/local/lib/pkgconfig/ --with-python
    make
    make install
}
function p0f
{
    tar xvfz p0f-3.09b.tgz
    cd p0f-3.09b
    ./build.sh
}

function main
{
    echo -e "${green} [*] Configuring OSmap${nc}"
    packages
    downloads
    fixbuf
    yaf
    silk
    p0f

}
main

