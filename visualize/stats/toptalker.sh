#!/bin/bash
# Top talker IP info

for i in $(cat ../osmap.csv | cut -d "," -f 3 | sort -n) ; do echo $i > toptalker.txt;done

output="$(grep $(cat toptalker.txt) ../osmap.csv)"
ip="$(echo $output| cut -d"," -f 1)"
os="$(echo $output| cut -d"," -f 2)"
conv="$(echo $output| cut -d "," -f 3)"


toptalker= "$(echo "Top Talker:" $ip)"
TTos="$(echo "OS:" $os)"
TTCov="$(echo "Conversations:" $conv)"

printf $toptalker'\n'$TTos'\n'$TTconv > toptalker.txt
