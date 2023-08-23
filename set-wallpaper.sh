#!/usr/bin/env bash
FILE=${FILE:-~/tmp/random-wallpaper}
current_resolution=$(xdpyinfo | grep -oP 'dimensions:\s+\K\S+')
# echo $current_resolution
if !$WALLHAVEN_API_KEY; then
    echo "API_KEY is not set, go to https://wallhaven.cc/join to get a wallhaven API key"
    exit 1
fi
api_url="https://wallhaven.cc/api/v1/search?api_key=$WALLHAVEN_API_KEY&categories=010&purity=100&sorting=random&order=desc&resolutions=$current_resolution"
# echo $api_url
download_url=$(curl -L "$api_url" | jq -r '.data[0].path')
# echo $download_url
curl -L "$download_url" -o "$FILE"
feh --bg-fill "$FILE"

