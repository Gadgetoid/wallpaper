from PIL import Image

DESKTOP_WIDTH = 1920
DESKTOP_HEIGHT = 1080

TILE_WIDTH = 64
TILE_HEIGHT = 64

TILES_X = int(DESKTOP_WIDTH / TILE_WIDTH)
TILES_Y = int(DESKTOP_HEIGHT / TILE_HEIGHT)

def get_filename(x, y, extension='png'):
    return "tiles/{x:02}-{y:02}.{ext}".format(x=x, y=y, ext=extension)

def load_tile(x, y):

    extensions = ['png', 'jpg']

    for ext in extensions:
        filename = get_filename(x, y, extension=ext)
        try:
            tile = Image.open(filename).convert("RGBA").resize((TILE_WIDTH, TILE_HEIGHT))
            print("Found: {}".format(filename))
            return tile
        except IOError:
            pass

    row = y % 2
    col = (x + row) % 2

    grey = 5 + (5 * col)
    tile = Image.new("RGBA", (TILE_WIDTH, TILE_HEIGHT), (grey, grey, grey, 255))

    return tile

if __name__ == "__main__":
    wallpaper = Image.new("RGBA", (DESKTOP_WIDTH, DESKTOP_HEIGHT), (0, 0, 0, 255))

    for x in range(TILES_X):
        for y in range(TILES_Y):
            offset_x = x * TILE_WIDTH
            offset_y = y * TILE_HEIGHT
            tile = load_tile(x, y)
            wallpaper.paste(tile, (offset_x, offset_y))

    wallpaper.save("wallpaper.png")
