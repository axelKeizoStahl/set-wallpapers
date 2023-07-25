# set-wallpapers
run python3 get-wallpapers.py to download wallpapers onto ~/Downloads/images/
then chmod +x ./set-wallpaper.sh and run it 
make sure you have feh installed as set-wallpaper.sh uses feh to set wallpaper
you can change the link that the python script downloads from though it looks for the <img> tag and data-src link which are specific to this website.
You also need an internet connection
For python packages install re, os, requests, requests_html
