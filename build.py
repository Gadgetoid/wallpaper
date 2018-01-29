from PIL import Image, ImageDraw
import glob
import random
import colorsys

DESKTOP_WIDTH = 1920
DESKTOP_HEIGHT = 1080

TILE_WIDTH = 64
TILE_HEIGHT = 64

TILES_X = int(DESKTOP_WIDTH / TILE_WIDTH)
TILES_Y = int(DESKTOP_HEIGHT / TILE_HEIGHT)

found_count = 0
found_total = TILES_X * TILES_Y

def place_tiles():
    global found_count
    grid = [[None for y in range(TILES_Y)] for x in range(TILES_X)]
    random_tiles = []

    tiles = []
    for ext in ['png', 'jpg']:
        tiles.extend(glob.glob("tiles/*.{}".format(ext)))

    found_count = len(tiles)
    
    for tile in tiles:
        img = Image.open(tile).convert("RGBA").resize((TILE_WIDTH, TILE_HEIGHT), resample=Image.BILINEAR)

        filename = tile.split('/')[-1]
        fname, fext = filename.split('.')
        for delimiter in ['x','-','_','X']:
            if delimiter in fname:
                fname = fname.split(delimiter)
                break

        if len(fname) == 2:
            try:
                x = int(fname[0])
                y = int(fname[1])
                print("Adding {} to {}x{}".format(filename, x, y))
                grid[x][y] = img
                continue
            except (ValueError, IndexError):
                pass

        print("Adding {} to random".format(filename))
        random_tiles.append(img)

    for random_tile in random_tiles:

        while has_slot(grid):
            x = random.randint(0, TILES_X-1)
            y = random.randint(0, TILES_Y-1)
            if grid[x][y] is None:
                grid[x][y] = random_tile
                break

    return grid
        
def has_slot(grid):
    for x in range(TILES_X):
        for y in range(TILES_X):
            if grid[x][y] is None:
                return True
    return False

if __name__ == "__main__":
    wallpaper = Image.new("RGBA", (DESKTOP_WIDTH, DESKTOP_HEIGHT), (0, 0, 0, 255))

    draw = ImageDraw.Draw(wallpaper)

    for y in range(TILES_Y):
        val = (1.0 / TILES_Y) * y
        for x in range(TILES_X):
            hue = (1.0 / TILES_X) * x
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, val)]
            rainbow_x = x * TILE_WIDTH
            rainbow_y = y * TILE_HEIGHT
            draw.rectangle((rainbow_x, rainbow_y, rainbow_x+TILE_WIDTH, rainbow_y+TILE_HEIGHT), fill=(r, g, b, 255), outline=None)

    grid = place_tiles()

    for x in range(TILES_X):
        for y in range(TILES_Y):
            offset_x = x * TILE_WIDTH
            offset_y = y * TILE_HEIGHT
            tile = grid[x][y]

            if tile is None:
                row = y % 2
                col = (x + row) % 2
                grey = 5 + (5 * col)
                tile = Image.new("RGBA", (TILE_WIDTH, TILE_HEIGHT), (255, 255, 255, grey))

            wallpaper.paste(tile, (offset_x, offset_y), mask=tile)

    print("Found {found} tiles out of a {total} total. {remaining} tiles left!\nProgress: {prog:1.1f}%".format(
        found=found_count,
        total=found_total,
        remaining=found_total-found_count,
        prog=(100.0/found_total) * found_count
    ))

    wallpaper.save("wallpaper.png")
