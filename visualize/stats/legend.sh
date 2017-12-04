#!/bin/bash
# creates legend from csv
os="$(cat visualize/osmap.csv | cut -d "," -f 2 | sort | uniq | grep -v "category")"
printf "LIST OF OPERATING SYSTEMS: \n" > visualize/stats/legend.txt
total="$(cat visualize/osmap.csv | wc -l)"
printf "Total Clients : $total\n" >> visualize/stats/legend.txt
printf "   [+] $os\n" >> visualize/stats/legend.txt
