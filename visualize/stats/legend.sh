#!/bin/bash
# creates legend from csv
os="$(cat visualize/osmap.csv | cut -d "," -f 2 | sort | uniq | grep -v "category")"
grepC="$(grep -c visualize/osmap.csv "$os")"
printf "$os : $grepC\n" >> visualize/stats/legend.txt

