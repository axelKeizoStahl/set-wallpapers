# set-wallpapers
I changes to an api, wallhaven.cc specifically.
This means you need a wallhaven api key.
Just go to wallhaven.cc/join to create an account and you'll see the api key in the profile/settings
Then hop onto a terminal and export the key by writing:
`export WALLAVEN_API_KEY="your api key"`
replacing "your api key" with your actual key.
After git cloning the repo you should make the script an executable
`chmod +x set-wallpaper.sh`
You also need to install feh, which is used to set the wallpaper
There is a purity option that is set to 100 where 1 is on and 0 is off, nsfw and scetchy is off on purpose.
Then run it
`./set-wallpaper.sh`
Or put it in you rc files somewhere.
