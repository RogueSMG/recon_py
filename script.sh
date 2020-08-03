#!/bin/bash

domain=$1

mkdir $1
cd $1
assetfinder --subs-only $1 > subs_assetfinder
python /home/parth/tools/Sublist3r/sublist3r.py -d $1 -o subs_sublist3r
amass enum --passive -d $1 -o subs_amass
findomain -t $1 -u subs_findomain
subfinder -d $1 -o subs_subfinder
cp subs_assetfinder > all_subs
cp subs_sublist3r >> all_subs
cp subs_amass >> all_subs
cp subs_findomain >> all_subs
cp subs_subfinder >> all_subs
echo "==============Resolving============"
cat all_subs | httprobe > hosts

regex="^(https:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$"

echo "==============Domains with 200 status code============="
cat hosts | while read line
do
	if [[ $line =~ $regex ]]; then
		echo $line >> final_subs
	fi
done
httpx -l final_subs -title -content-length -mc 200 -o alive.txt

echo "==============Running GAU============"
cat alive.txt | gau > gau_data

