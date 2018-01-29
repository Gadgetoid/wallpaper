# Wallpaper

Picking wallpaper is difficult, so it's time to bring the power of the internet to bear and crowdsource it instead!

Submit your tile into tiles as a 64x64 pixel PNG image and this script will hopefully slurp them up and turn them into an abominable mess of a wallpaper.

# Tile Naming

Your tile *should* be named XX-YY.jpg or XX-YY.png, my desktop is 1920x1080 pixels, and the X and Y coordinates are zero indexed, which gives you the range:

* x = 0 to 29
* y = 0 to 15
* `0, 0` is the top left of the image so: `01-02.png` or `29-15.png` are valid and will be placed on the second row, third column, and 30th row, 16th column respectively.

Any invalid images will be randomly placed while space is available, but you should pick a slot while stocks last!

Have fun! For updates and feedback follow me on:

* Twitter: https://twitter.com/gadgetoid
* Discord: https://discord.gg/8wRN4WB
* Patron: https://patreon.com/gadgetoid

# Etiquette

I don't want too many rules, but put forth this simple code of etiquette:

* Unless it violates the etiquette, I *must* merge your PR
* Smut images are unimaginative, you're better than that
* Racist/hateful images are also unimaginative, seriously, why do I need to even say this?
* Trampling on other people's tiles is kinda mean, but if they're hogging the whole darn wallpaper they kinda deserve it
* Don't PR against the build.py unless you have a bugfix/improvement, I'm not dumb enough to automate it right out of git!

# Roadmap

* Add wallpaper WIDTH/HEIGHT command-line options to build.py
* Add tile WIDTH/HEIGHT command-line options to build.py

What if every image had an accompanying data file that dictated its x/y position/rotation, etc? Could we make this a crazy graffiti wall of transparent PNGs?

# Building Your Own

Most of the magic happens in the build.py script, where you can set your own wallpaper and tile size. This script outputs `wallpaper.png`

For the convinience of Windows 10 users (of which I am one) I have packaged build.py up into build.exe, which should *just work* for you.

On Windows 10 I use WallpaperChanger.exe to change the wallpaper from the command-line, it has been included for convinience.

You can find the source and LICENSE here: https://github.com/philhansen/WallpaperChanger

To build and set the wallpaper:

```
build.exe
WallpaperChanger.exe wallpaper.png
```

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
