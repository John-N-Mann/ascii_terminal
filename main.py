import os, sys, random
from tkinter import Y
import pygame
from PIL import Image

CURRENT_IMAGE = 'PY/ASCII_TERMINAL/candy.png'

SCALE = 4
RAW_WIDTH = 0
RAW_HEIGHT = 0
RGB_WIDTH = 0
RGB_HEIGHT = 0
RGB_MATRIX = [[(0,0,0)]]
ALPHA_MATRIX = [[(0)]]
CHAR_MATRIX = [['`']]
ASCIISTRING = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$$' # 67 characters long



def readimage(im) -> Image: # use pillow to load PNG file and read size of image
    global RAW_WIDTH
    global RAW_HEIGHT
    print('\nLoading image into I/O stream.')
    imagesource = Image.open(im)
    RAW_WIDTH = imagesource.size[0]
    RAW_HEIGHT = imagesource.size[1]
    print('\nImage loaded. Image size is: ' + str(RAW_WIDTH) + 'x' + str(RAW_HEIGHT) + '\n')
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
#for x in range(0, RGB_WIDTH - 1):
#    for y in range(0, RGB_HEIGHT - 1):
#       # print(RGB_MATRIX[x][y])

# average the pixels for monochrome format
# Average = (R + G + B) / 3
# Lightness = max(R, G, B) + min(R, G, B)) / 2
# Luminosity = 0.21R + 0.72G + 0.07B

# create new matrix for alpha values
ALPHA_MATRIX = [[(0)] * RAW_HEIGHT for i in range(RAW_WIDTH)]

# convert RGB into Alpha (using averaging formula)
for x in range(0, RGB_WIDTH - 1):
    for y in range(0, RGB_HEIGHT - 1):
        ALPHA_MATRIX[x][y] = int((RGB_MATRIX[x][y][0] + RGB_MATRIX[x][y][1] + RGB_MATRIX[x][y][2]) / 3)

# testing
print('Test pixel: ' + str(ALPHA_MATRIX[(RGB_WIDTH - random.randint(0, RGB_WIDTH - 1))][(RGB_HEIGHT - random.randint(0, RGB_HEIGHT - 1))]))


# take ALPHA_MATRIX and create a new matrix based on any dimension -- in this case scaling by four
prev_height = RGB_HEIGHT
prev_width = RGB_WIDTH
new_height = prev_height/4
new_width = prev_width/4

def average_pixels(loc: tuple, scale = 4) -> int:
    avg = 0
    div = 0
    for x in range(scale):
        for y in range(scale):
            avg += ALPHA_MATRIX[int(loc[0] + x)][int(loc[1] + y)]
            div += 1
    num = int(avg/div)
    return num

print('Average is: ' + str(average_pixels((24, 23))))

def descale_matrix(mtrx, scale = 4):
    mtrx = [[(0)] * (int(RAW_HEIGHT/scale)) for i in range((int(RAW_WIDTH/scale)))]
    wmtrx = (len(mtrx))
    hmtrx = (len(mtrx[0]))
    for x in range(wmtrx):
        for y in range(hmtrx):
            avg = average_pixels(((x*scale), (y*scale)), scale)
            mtrx[x][y] = avg
    return mtrx

newmatrix = descale_matrix(ALPHA_MATRIX, SCALE)
newmatrix_w = len(newmatrix)
newmatrix_h = len(newmatrix[0])
print(newmatrix_w)
print(newmatrix_h)


# Convert the alpha brightness to a corresponding ASCII character -- maximum RGB value is 255 -- 67 ASCII characters to convert to

CHAR_MATRIX = [['`'] * newmatrix_h for i in range(newmatrix_w)] # set character matrix

# iterate thru and convert matrix to characters
for x in range(newmatrix_w):
    for y in range(newmatrix_h):
        ref = int(int(newmatrix[x][y]) / 3.8)
        if ref > 65:
            ref = 65
        CHAR_MATRIX[x][y] = ASCIISTRING[ref]

print('Converting ALPHA pixels to CHAR data.\n')

print('Test pixel: ' + str(CHAR_MATRIX[(newmatrix_w - random.randint(0, newmatrix_w - 1))][(newmatrix_h - random.randint(0, newmatrix_h - 1))]) + '\n')

#tcod.console_set_custom_font('PY/ASCII_TERMINAL/MANNfont10x10_gs_tc.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
#tcod.console_init_root(RGB_WIDTH, RGB_HEIGHT, 'JMANN_ASCII_TERMINAL', False)
#tcod.console_flush()






###################
## PYGAME TESTS ###
###################

## TEST OUTPUT OF CHAR MATRIX ###
# Initialize Pygame and create a basic window of image size
pygame.init()
pygame.display.set_caption('ASCII_ART')

pygame.font.get_default_font()
asciifont = pygame.font.Font(pygame.font.get_default_font(), SCALE)

screen = pygame.display.set_mode((newmatrix_w * SCALE, newmatrix_h * SCALE))

for y in range(newmatrix_h):
        for x in range(newmatrix_w):
            surface = asciifont.render(CHAR_MATRIX[x][y], True, (255, 255, 255))
            screen.blit(surface, (x * SCALE, y * SCALE))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()




# ### TEST OUTPUT OF RGB VALUE ###

# screen = pygame.display.set_mode((RGB_WIDTH, RGB_HEIGHT), pygame.RESIZABLE)
# square = pygame.Surface((1, 1))
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

#     for y in range(0, RGB_HEIGHT - 1):
#         for x in range(0, RGB_WIDTH - 1):
#             square.fill(RGB_MATRIX[x][y])
#             screen.blit(square, pygame.Rect((x + 1), (y + 1), 1, 1))
#     pygame.display.flip()


