#!/bin/bash
# Top talker IP info

for i in $(cat visualize/osmap.csv | cut -d "," -f 3 | sort -n) ; do echo $i > visualize/stats/toptalker.txt;done

output="$(grep $(cat visualize/stats/toptalker.txt) visualize/osmap.csv)"
ip="$(echo $output| cut -d"," -f 1)"
os="$(echo $output| cut -d"," -f 2)"
conv="$(echo $output| cut -d "," -f 3)"


echo "$(echo "Top Talker:" $ip;
echo "OS:" $os;
echo "Conversations:" $conv)" > visualize/stats/toptalker.txt

