#!/bin/bash

path="~/Downloads/images"

backgrounds_dir=$(eval echo $path)

image_files=("$backgrounds_dir"/*.jpg "$backgrounds_dir"/*.jpeg "$backgrounds_dir"/*.png)

selected_image="${image_files[RANDOM % ${#image_files[@]}]}"
selected_image_2="${image_files[RANDOM % ${#image_files[@]}]}"

screen_size=$(xrandr | grep ' connected' | awk '{print $3}' | cut -f1 -d"+")

if xrandr | grep -q 'HDMI1 connected'
then
    feh_command="feh --bg-fill $selected_image $selected_image &"
    eval "$feh_command"
fi

feh_command="feh --bg-fill $selected_image &"
eval "$feh_command"
