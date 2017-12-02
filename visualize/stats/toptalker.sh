#!/bin/bash
# Top talker IP info

for i in $(cat ../osmap.csv | cut -d "," -f 3 | sort -n) ; do echo $i > toptalker.txt;done

output="$(grep $(cat toptalker.txt) ../osmap.csv)"
ip="$(echo $output| cut -d"," -f 1)"
os="$(echo $output| cut -d"," -f 2)"
conv="$(echo $output| cut -d "," -f 3)"


echo "Top Talker:" $ip;
echo "OS:" $os;
echo "Conversations:" $conv >> toptalker.txt

