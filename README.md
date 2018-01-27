# Wallpaper

Picking wallpaper is difficult, so it's time to bring the power of the internet to bear and crowdsource it instead!

Submit your tile into tiles as a 64x64 pixel PNG image and this script will hopefully slurp them up and turn them into an abominable mess of a wallpaper.

# Tile Naming

Your tile *must* be named XX-YY.jpg or XX-YY.png, my desktop is 1920x1080 pixels, and the X and Y coordinates are zero indexed, which gives you the range:

* x = 0 to 29
* y = 0 to 15

So: `01-02.png` or `29-15.png` are valid.

Have fun! For updates follow me on:

* Twitter: https://twitter.com/gadgetoid
* Discord: https://discord.gg/8wRN4WB
* Patron: https://patreon.com/gadgetoid

# Etiquette

I don't want too many rules, but put forth this simple code of etiquette:

* Unless it violates the etiquette, I've got to merge your PR
* Smut images are unimaginative, you're better than that
* Racist/hateful images are also unimaginative, seriously, why do I need to even say this?
* Trampling on other people's tiles is kinda mean, but if they're hogging the whole darn wallpaper they kinda deserve it
* Don't PR against the build.py unless you have a bugfix/improvement, I'm not dumb enough to automate it right out of git!

# Roadmap

What if ever image had an accompanying data file that dictated its x/y position/rotation, etc? Could we make this a crazy graffiti wall of transparent PNGs?

# Building Your Own

Most of the magic happens in the build.py script, where you can set your own wallpaper and tile size.

My build/set script on Windows 10 currently looks something like this. It's... heinous and I don't even know if it will work reliably:

```
#!/bin/bash
git pull pullonly master
wsl bash -c "cd /path/to/git/wallpaper && python build-safe.py"
cp wallpaper.png ~/AppData/Roaming/Microsoft/Windows/Themes/TranscodedWallpaper
rm ~/AppData/Roaming/Microsoft/Windows/Themes/CachedFiles/*1920_1080*.jpg
rundll32.exe user32.dll, UpdatePerUserSystemParameters ,1 ,True
```

So- briefly:

* I have a pullonly origin set up so I can passwordless pull the latest tiles
* I have a copy of the build file named `build-safe.py` that hasn't been tampered with ;) (ahaha, this is doomed to fail)
* The wallpaper png file is copied to the location Windows 10 stores its wallpaper file
* Delete the cached wallpaper file
* Update the user prefs to display the new file

# Fund my insanity

I originally planned for this project to be an insane GoFundMe where I fund the purchase of a shiny new monitor (both mine are 8+ years old)
by rewarding every donator with a 64x64 slice of my wallpaper *forever*.

This was a bad fit for GoFundMe though, and my antics feel a little out of place alongside the genuine impassioned pleas for help.

Also GoFundMe doesn't really *do* rewards, and had no framework in place for me to keep track of donators and make sure they got their slot.

So, this is the result; a git-based system for giving users control over 64x64 chunks of my wallpaper.

In fact you can clone and modify this script to crowdsource X by Y chunks of any size wallpaper or image via Git.

I still need your support, though, and I want to dedicate more of my time to random acts of coding kindness and insanity.
If you appreciate all the useful (and silly) stuff that I do then toss me a dollar on Patreon, it's super appreciated:

https://www.patreon.com/gadgetoid
