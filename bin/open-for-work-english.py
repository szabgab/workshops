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

    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 160)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    add_text(
        draw = draw,
        text = "I am open for my next assignment",
        rtl  = False,
        size = 70,
        xy   = (50, 30),
    )

    add_text(
        draw = draw,
        text = "- Introduce test automation",
        rtl  = False,
        size = 65,
        xy   = (50, 170),
    )
    add_text(
        draw = draw,
        text = "- Setup CI system",
        rtl  = False,
        size = 65,
        xy   = (50, 250),
    )

    add_text(
        draw = draw,
        text = "- Modernize code base (Python, Perl)",
        rtl  = False,
        size = 65,
        xy   = (50, 330),
    )

    add_text(
        draw = draw,
        text = "- Create Docker containers",
        rtl  = False,
        size = 65,
        xy   = (50, 410),
    )



    add_text(
        draw = draw,
        text = "Gábor Szabó",
        rtl  = False,
        size = 50,
        xy   = (750, 620),
    )

    embed_image(img=img, filename='gabor2_612x612.jpg', size=(200, 200), box=(width-200-10, 500))
    #embed_image(img=img, filename='mojolicious.png', box=(10, 10), mask=True)

    img.save(png_filepath)
    img.show()


main()
