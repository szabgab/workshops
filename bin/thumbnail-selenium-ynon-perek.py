import os
from PIL import Image, ImageDraw, ImageFont
from mypil import add_text, add_date, embed_image

width  = 1280
height = 720

# background_color = '#eb8634'
#background_color = '#ebb434'
background_color = '#DDDDDD'

root = os.path.dirname(os.path.dirname(__file__))
#print(root)

def main():
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    #print(png_filename)

    png_filepath = os.path.join(root, 'images', png_filename)
    #print(png_filepath)

    img = Image.new('RGB', (width, height), color=background_color)

    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 160)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    add_text(
        draw = draw,
        text = "Web application testing",
        rtl  = False,
        size = 70,
        xy   = (240, 30),
    )

    add_text(
        draw = draw,
        text = "with",
        rtl  = False,
        size = 70,
        xy   = (540, 180),
    )


    add_text(
        draw = draw,
        text = "Selenium and Python",
        rtl  = False,
        size = 80,
        xy   = (240, 330),
    )
#
#    add_text(
#        draw = draw,
#        text = "and Gábor Szabó",
#        rtl  = False,
#        size = 80,
#        xy   = (50, 540),
#    )

    #add_text(
    #    draw = draw,
    #    text = "in less than",
    #    rtl  = False,
    #    size = 60,
    #    xy   = (250, 440),
    #)

    #add_text(
    #    draw = draw,
    #    text = "14 minutes",
    #    rtl  = False,
    #    size = 60,
    #    xy   = (250, 540),
    #)


    embed_image(img=img, filename='selenium-green.png', size=(200, 208), box=(10, 10))
    embed_image(img=img, filename='python.png',         size=(200, 200), box=(width-200-10, 10), mask=True)
    embed_image(img=img, filename='ynon_perek.jpeg',    size=(200, 200), box=(10, 500))
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(200, 200), box=(width-200-10, 500))

    img.save(png_filepath)
    img.show()


main()
