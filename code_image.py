#!usr/bin/python
# coding: utf-8
"""windows跑不了"""

import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndChar():
    return chr(random.randint(65,90))

def rndColor():
    return (random.randint(64,255), random.randint(64,255),
            random.randint(64,255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127),
            random.randint(32, 127))

width = 240
height = 60

# 建一个240*60的全白的RGB image
image = Image.new('RGB', (width, height), (255,255,255))

font = ImageFont.truetype('/usr/share/fonts/truetype/padauk/Padauk.ttf', 36)

draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

for t in range(4):
    draw.text((60*t+10, 10), rndChar(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')
