#!/bin/bash
echo Enter [1] to launch the splash server or [2] to run a splashshell
read choice

if [ $choice -eq '1' ]
then
    sudo docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash
    exit 1
elif [ $choice -eq '2' ]
then
    a="scrapy shell 'http://localhost:8050/render.html?url="
    c="&wait=5'"
    echo Please enter the url you wish to use with the scrapy-splash shell
    read url
    echo $url
    launch=$a$url$c
    echo -e $launch > ln.sh
    chmod +x ln.sh
    gnome-terminal -x ~/Google\ Drive/Coding/Scrapy/findJob/ln.sh
else
    echo "Error: Incorrect Use"
    exit 1
fi