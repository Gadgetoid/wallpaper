#!/usr/bin/env python
from PIL import Image, ImageDraw
import glob
import random
import colorsys
import argparse
import os

DEFAULT_WIDTH = 1920
DEFAULT_HEIGHT = 1080

DEFAULT_TILE_WIDTH = 64
DEFAULT_TILE_HEIGHT = 64

DEFAULT_ADD_RAINBOWS = True

class Wallpaperer():
    def __init__(self, wallpaper_width=1920, wallpaper_height=1080, tile_width=64, tile_height=64, verbose=False, smooth=True):
        self.found_count = 0
        self.wallpaper_width = wallpaper_width
        self.wallpaper_height = wallpaper_height
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.verbose = verbose
        self.formats = ('png', 'jpg', 'jpeg')
        self.smooth = smooth

    @property
    def tiles_x(self):
        return self.wallpaper_width // self.tile_width

    @property
    def tiles_y(self):
        return self.wallpaper_height // self.tile_height

    @property
    def tile_count(self):
        return self.tiles_x * self.tiles_y

    def place_tiles(self, directory="tiles"):
        grid = [[None for y in range(self.tiles_y)] for x in range(self.tiles_x)]
        random_tiles = []

        tiles = []
        for ext in self.formats:
            tiles.extend(glob.glob(os.path.join(directory, "*.{}".format(ext))))

        self.found_count = len(tiles)
        
        for tile in tiles:
            img = Image.open(tile).convert("RGBA").resize((self.tile_width, self.tile_height), resample=Image.BILINEAR if self.smooth else Image.NEAREST)

            filename = os.path.split(tile)[-1]
            fname, fext = filename.split('.')
            for delimiter in ['x','-','_','X']:
                if delimiter in fname:
                    fname = fname.split(delimiter)
                    break

            if len(fname) == 2:
                try:
                    x = int(fname[0])
                    y = int(fname[1])
                    if self.verbose: print("Adding {} to {}x{}".format(filename, x, y))
                    grid[x][y] = img
                    continue
                except (ValueError, IndexError):
                    pass

            if self.verbose: print("Adding {} to random".format(filename))
            random_tiles.append(img)

        for random_tile in random_tiles:
            while self.has_slot(grid):
                x = random.randint(0, self.tiles_x-1)
                y = random.randint(0, self.tiles_y-1)
                if grid[x][y] is None:
                    grid[x][y] = random_tile
                    break

        return grid
            
    def has_slot(self, grid):
        for x in range(self.tiles_x):
            for y in range(self.tiles_y):
                if grid[x][y] is None:
                    return True
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate tiled wallpaper!')
    parser.add_argument('--rainbows', type=bool, help='add rainbows!', default=DEFAULT_ADD_RAINBOWS)
    parser.add_argument('--tiles_x', type=int, help='number of horizontal tiles, overrides width/height', default=None)
    parser.add_argument('--tiles_y', type=int, help='number of vertical tiles, overrides width/height', default=None)
    parser.add_argument('--tilewidth', type=int, help='tile width in pixels (default: {}px)'.format(DEFAULT_TILE_WIDTH), default=DEFAULT_TILE_WIDTH)
    parser.add_argument('--tileheight', type=int, help='tile height in pixels (default: {}px)'.format(DEFAULT_TILE_HEIGHT), default=DEFAULT_TILE_HEIGHT)
    parser.add_argument('--width', type=int, help='wallpaper width in pixels (default: {}px)'.format(DEFAULT_WIDTH), default=DEFAULT_WIDTH)
    parser.add_argument('--height', type=int, help='wallpaper height in pixels (default: {}px)'.format(DEFAULT_HEIGHT), default=DEFAULT_HEIGHT)
    parser.add_argument('--insanity', action='store_true', help='use a proper coordinate system for geniuses! (default: your fault!)', default=False)
    parser.add_argument('--nearest', action='store_true', help='use nearest filtering to resize tiles', default=False)
    parser.add_argument('--filename', type=str, help='filename to save as (defaut: wallpaper.png)', default='wallpaper.png')

    args = parser.parse_args()

    if args.tiles_x is not None and args.tiles_y is not None:
        args.tilewidth = args.width // args.tiles_x
        args.tileheight = args.height // args.tiles_y

    wallpaperer = Wallpaperer(
        wallpaper_width=args.width,
        wallpaper_height=args.height,
        tile_width=args.tilewidth,
        tile_height=args.tileheight,
        smooth=not args.nearest)

    wallpaper = Image.new("RGBA", (args.width, args.height), (0, 0, 0, 255))

    if args.rainbows:
        draw = ImageDraw.Draw(wallpaper)

        for y in range(wallpaperer.tiles_x):
            val = (1.0 / wallpaperer.tiles_y) * y
            for x in range(wallpaperer.tiles_x):
                hue = (1.0 / wallpaperer.tiles_y) * x
                r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, val)]
                rainbow_x = x * wallpaperer.tile_width
                rainbow_y = y * wallpaperer.tile_height
                draw.rectangle((rainbow_x, rainbow_y, rainbow_x+wallpaperer.tile_width, rainbow_y+wallpaperer.tile_height), fill=(r, g, b, 255), outline=None)

    grid = wallpaperer.place_tiles()

    for x in range(wallpaperer.tiles_x):
        for y in range(wallpaperer.tiles_y):
            offset_x = x * wallpaperer.tile_width
            offset_y = y * wallpaperer.tile_height

            if args.insanity:
                tile = grid[x][y]
            else:
                tile = grid[x][wallpaperer.tiles_y - 1 - y]

            if tile is None:
                row = y % 2
                col = (x + row) % 2
                grey = 5 + (5 * col)
                tile = Image.new("RGBA", (wallpaperer.tile_width, wallpaperer.tile_height), (255, 255, 255, grey))

            wallpaper.paste(tile, (offset_x, offset_y), mask=tile)

    print("Found {found} tiles out of a {total} total. {remaining} tiles left!\nProgress: {prog:1.1f}%".format(
        found=wallpaperer.found_count,
        total=wallpaperer.tile_count,
        remaining=wallpaperer.tile_count-wallpaperer.found_count,
        prog=(100.0/wallpaperer.tile_count) * wallpaperer.found_count
    ))

    wallpaper.save(args.filename)
