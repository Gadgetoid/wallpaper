# Wallpaper

Picking wallpaper is difficult, so it's time to bring the power of the internet to bear and crowdsource it instead!

Submit your tile into tiles as a 64x64 pixel PNG image and this script will hopefully slurp them up and turn them into an abominable mess of a wallpaper.

# Etiquette

I don't want too many rules, but put forth this simple code of etiquette:

* Unless it violates the etiquette, I've got to merge your PR
* Smut images are unimaginative, you're better than that
* Racist/hateful images are also unimaginative, seriously, why do I need to even say this?
* Trampling on other people's tiles is kinda mean, but if they're hogging the whole darn wallpaper they kinda deserve it
* Don't PR against the build.py unless you have a bugfix/improvement, I'm not dumb enough to automate it right out of git!

# Roadmap

What if ever image had an accompanying data file that dictated its x/y position/rotation, etc? Could we make this a crazy graffiti wall of transparent PNGs?

# Building

My build/set script on Windows 10 currently looks like this. It's... heinous and I don't even know if it will work reliably:

```
#!/bin/bash
git pull pullonly master
wsl bash -c "cd /path/to/git/wallpaper && python build-safe.py"
cp wallpaper.png ~/AppData/Roaming/Microsoft/Windows/Themes/TranscodedWallpaper
rundll32.exe user32.dll, UpdatePerUserSystemParameters
sleep 1
rundll32.exe user32.dll, UpdatePerUserSystemParameters
```

So- briefly:

* I have a pullonly origin set up so I can passwordless pull the latest tiles
* I have a copy of the build file named `build-safe.py` that hasn't been tampered with ;) (ahaha, this is doomed to fail)
* The wallpaper png file is copied to the location Windows 10 stores its wallpaper file
* The user prefs are updated, twice, or maybe more times because this seems to work unreliably!

