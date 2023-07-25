#!/bin/bash

path="~/Downloads/images"

backgrounds_dir="$(eval echo $path)"

image_files=("$backgrounds_dir"/*.jpg "$backgrounds_dir"/*.jpeg "$backgrounds_dir"/*.png)

selected_image="${image_files[RANDOM % ${#image_files[@]}]}"

feh --bg-scale "$selected_image"

