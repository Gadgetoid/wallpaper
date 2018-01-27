#!/bin/bash

# Currently I use Git Bash to run this script

# Update the local tile cache
git pull origin master

# Invoke WSL bash to use its Python to rebuild the image#
# This is awful and needs fixing with some kind of local venv
wsl bash -c "cd /mnt`pwd` && python build.py"

# Well this is easier!
# Source: https://github.com/philhansen/WallpaperChanger
./WallpaperChanger wallpaper.png

