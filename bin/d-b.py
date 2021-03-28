import os
import sys
from PIL import Image, ImageDraw, ImageFont
from mypil import add_text, add_date, embed_image

#width  = 720
#height = 720
width  = 224
height = 56

background_color = '#DDDDDD'

root = os.path.dirname(os.path.dirname(__file__))

def main():
    create_thumbnail()


def create_thumbnail():
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    png_filepath = os.path.join(root, 'images', png_filename)

    img = Image.new('RGB', (width, height), color=background_color)

    draw = ImageDraw.Draw(img)
    add_text(
        draw = draw,
        text = "d-b",
        rtl  = False,
#        size = 450,
#        xy   = (8, 150),
        size = 50,
        xy   = (70, 8),
    )

    img.save(png_filepath)
    img.show()


main()
