#!/bin/bash

relative_path="~/images"

backgrounds_dir="$(eval echo $relative_path)"

image_files=("$backgrounds_dir"/*.jpg "$backgrounds_dir"/*.jpeg "$backgrounds_dir"/*.png)

selected_image="${image_files[RANDOM % ${#image_files[@]}]}"

nitrogen --set-zoom-fill "$selected_image"

