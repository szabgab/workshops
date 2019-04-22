from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

if (len(sys.argv) < 2):
    exit("Usage: {} 'Company name'".format(sys.argv[0]))


in_file = 'images/code-maven-workshops-1600x900.png'  # 1600, 900
out_file = 'new.png'
text = sys.argv[1]

img = Image.open(in_file)
#print(img.size)

# Fonts: /usr/share/fonts/truetype/freefont/

draw = ImageDraw.Draw(img)
draw.polygon([(1600, 550), (1600, 900), (600, 900) ], fill = (255, 255, 255))

font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 70)
draw.text((1240, 670), 'Hosted by', (0, 0, 0), font=font)
draw.text((930, 790), text, (0, 0, 0), font=font)
img.save(out_file)

print(out_file + ' created')
