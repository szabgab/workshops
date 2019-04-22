from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

if (len(sys.argv) < 2):
    exit("Usage: {} 'Company name'".format(sys.argv[0]))


in_file = 'images/code-maven-workshops-1600x1200.png'  # 1600, 1200
out_file = 'new.png'
text = sys.argv[1]

img = Image.open(in_file)
#print(img.size)

# Fonts: /usr/share/fonts/truetype/freefont/

draw = ImageDraw.Draw(img)
draw.polygon([(1600, 700), (1600, 1200), (600, 1200) ], fill = (255, 255, 255))
font1 = ImageFont.truetype('Pillow/Tests/fonts/FreeMonoBold.ttf', 80)
draw.text((1160, 910), 'Hosted by', (0, 0, 0), font=font1)


font2 = ImageFont.truetype('Pillow/Tests/fonts/FreeMonoBold.ttf', 80)
draw.text((900, 1050), text, (0, 0, 0), font=font2)
img.save(out_file)

print(out_file + ' created')
