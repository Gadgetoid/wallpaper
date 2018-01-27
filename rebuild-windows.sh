#!/bin/bash

# Currently I use Git Bash to run this script

# Update the local tile cache
git pull origin master

# Invoke WSL bash to use its Python to rebuild the image#
# This is awful and needs fixing with some kind of local venv
wsl bash -c "cd /mnt`pwd` && python build.py"

# Copy the resulting wallpaper file over the cached "TranscodedWallpaper"
cp wallpaper.png ~/AppData/Roaming/Microsoft/Windows/Themes/TranscodedWallpaper

# Remove the cached cached (why, Windows?, WHY!?) jpg file
rm ~/AppData/Roaming/Microsoft/Windows/Themes/CachedFiles/*1920_1080*.jpg

# And force the wallpaper to update
# Sometimes this will work first try, sometimes not, there's no rhyme or reason to it
# The only failsafe method I can find is to keep smashing at the update until the cache file comes back
while [ ! -f ~/AppData/Roaming/Microsoft/Windows/Themes/CachedFiles/*1920_1080*.jpg ]; do
    rundll32.exe user32.dll,UpdatePerUserSystemParameters 1, True
    rundll32.exe user32.dll,UpdatePerUserSystemParameters
    sleep 1
done;
