from PIL import Image, ImageOps
import numpy as np

class Charmap:
    block    = " ░▒▓█" # Simulate pixels, more clear shapes
    mix      = " .o░▒▓█"
    simple   = " .*a@" # for high contrast 
    detailed = " .~*a@" # for normal contrast

char_ratio = .3

def brightness_chr_map(brightness, map):
    perc = brightness / 255
    pos = int( (len(map)-1) * perc )
    return map[pos]

def array_to_str(arr, map):
    result = ""
    for row in arr:
        for col in row:
            result += brightness_chr_map(col, map)

        result += "\n"

    return result[0:-1] # remove trailing \n

def convert(img, size, map=" .*a@") -> str:
    """
    Converts an image (PIL Image or filepath) into a string
    using theh gradient map for brightnesses
    """
    openimg = False
    if type(img) == str:
        img = Image.open(img)
        openimg = True

    altered = img.resize((size, int(size * char_ratio))) # resize & alter for characters not being square
    altered = ImageOps.grayscale(altered) # grayscale
    array   = np.asarray(altered)

    img.close()

    return array_to_str(array, map)
