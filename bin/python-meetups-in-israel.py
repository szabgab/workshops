import os
from PIL import Image, ImageDraw, ImageFont
from mypil import add_text, add_date, embed_image

width  = 1280
height = 720

# background_color = '#eb8634'
background_color = '#ebb434'
#background_color = '#DDDDDD'

root = os.path.dirname(os.path.dirname(__file__))
#print(root)

def main():
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    #print(png_filename)

    png_filepath = os.path.join(root, 'images', png_filename)
    #print(png_filepath)

    img = Image.new('RGB', (width, height), color=background_color)

    # Code-Maven Workshop

    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 160)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    add_text(
        draw = draw,
        text = "Python Meetups",
        rtl  = False,
        size = 120,
        xy   = (280, 100),
    )

    add_text(
        draw = draw,
        text = "In Israel",
        rtl  = False,
        size = 120,
        xy   = (280, 430),
    )

    isize = 350
    embed_image(img=img, filename='israel-flag-small.png', size=(250, 180), box=(width-250-70, height-180-160), mask=False)
    embed_image(img=img, filename='python.png', box=(30, 30), mask=True)

    img.save(png_filepath)
    img.show()


main()
