import os, sys
from PIL import Image

CURRENT_IMAGE = 'PY/ASCII_TERMINAL/candy.png'

def print_line(num = 12): # draws a simple line of # signs to separate terminal output
    print('#' * num)

def readimage(im) -> Image: # use pillow to load PNG file and read size of image
    print_line(48), print_line(48), print_line(48)
    print('\nLoading image into I/O stream.')
    imagesource = Image.open(im)
    print('\nImage loaded. Image size is: ' + str(imagesource.size))
    print_line(48), print_line(48), print_line(48)
    return imagesource

this = readimage(CURRENT_IMAGE)
this.show()

