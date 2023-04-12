#!/usr/bin/env python

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

if (len(sys.argv) < 2):
    exit("Usage: {} 'Company name'".format(sys.argv[0]))


in_file = 'docs/img/code-maven-workshops-1600x900.png'  # 1600, 900
full_file = 'full.png'
half_file = 'half.png'
text = sys.argv[1]

img = Image.open(in_file)
#print(img.size)

# Fonts: /usr/share/fonts/truetype/freefont/

draw = ImageDraw.Draw(img)
draw.polygon([(1600, 550), (1600, 900), (600, 900) ], fill = (255, 255, 255))

font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 70)
draw.text((1240, 670), 'Hosted by', (0, 0, 0), font=font)
draw.text((930, 790), text, (0, 0, 0), font=font)
img.save(full_file)
print(full_file + ' created')


size = (img.size[0]/2,  img.size[1]/2)
img.thumbnail(size)
img.save(half_file)
print(half_file + ' created')
