import os, sys, random
from PIL import Image

CURRENT_IMAGE = 'PY/ASCII_TERMINAL/candy.png'

RAW_WIDTH = 0
RAW_HEIGHT = 0
RGB_WIDTH = 0
RGB_HEIGHT = 0
RGB_MATRIX = [[(0,0,0)]]

def print_line(num = 12): # draws a simple line of # signs to separate terminal output
    print('#' * num)

def readimage(im) -> Image: # use pillow to load PNG file and read size of image
    global RAW_WIDTH
    global RAW_HEIGHT
    print_line(48), print_line(48), print_line(48)
    print('\nLoading image into I/O stream.')
    imagesource = Image.open(im)
    RAW_WIDTH = imagesource.size[0]
    RAW_HEIGHT = imagesource.size[1]
    print('\nImage loaded. Image size is: ' + str(RAW_WIDTH) + 'x' + str(RAW_HEIGHT) + '\n')
    print_line(48), print_line(48), print_line(48)
    return imagesource

this = readimage(CURRENT_IMAGE)
print('\n')

# Construct pixel matrix -- 2D list of tuples storing RGB data at each pixel
RGB_MATRIX = [[(0, 0, 0)] * RAW_HEIGHT for i in range(RAW_WIDTH)]
print('\nCreated pixel matrix.\n')

# Convert RGBA to RGB
for x in range(0, RAW_WIDTH - 1):
    for y in range(0, RAW_HEIGHT - 1):
        RGB_MATRIX[x][y] = (this.getpixel((x,y))[0], this.getpixel((x,y))[1], this.getpixel((x,y))[2])
print('\nConverted RGBA pixels to RGB')
# Grab a random pixel and test content
print('Test pixel: ' + str(RGB_MATRIX[(RAW_WIDTH - random.randint(0, RAW_WIDTH - 1))][(RAW_HEIGHT - random.randint(0, RAW_HEIGHT - 1))]))

# Confirm pixel matrix size -- both 'length' and 'height'
RGB_WIDTH = (len(RGB_MATRIX))
RGB_HEIGHT = (len(RGB_MATRIX[0]))
assert RGB_WIDTH == RAW_WIDTH
assert RGB_HEIGHT == RAW_HEIGHT

# Prove you can iterate thru each pixel
for x in range(0, RGB_WIDTH - 1):
    for y in range(0, RGB_HEIGHT - 1):
        print(RGB_MATRIX[x][y])