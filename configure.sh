#!/bin/bash
#Configuration file
#to install YAF and SiLK
#for netflow analysis
#must run with sudo

red='\033[0;31m'
green='\033[0;32m'
nc='\033[0m'
wd=$(pwd)
function packages
{
    echo -e "${green} Installing required packages${nc}"
    echo -e "${green}[*] Installing libglib2.0${nc}"
    apt-get install git libglib2.0-dev
    echo -e "${green}[*] Installing libpcap${nc}"
    apt-get install libpcap-dev
    echo -e "${green}[*] Installing python-dev${nc}"
    apt-get install python-dev python-pip
    echo -e "${green} [+] Completed installation of required packages${nc}"

}

function p0f
{
    cd $wd
    git clone https://github.com/obormot/p0f-JSON
    cd p0f-JSON
    ./build.sh
}

function main
{
    echo -e "${green} [*] Configuring OSmap${nc}"
    packages
    p0f
    echo -e "${green}[+] oSmap configured${nc}"

}
main

