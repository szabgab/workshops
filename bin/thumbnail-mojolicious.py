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
        text = "Live web development",
        rtl  = False,
        size = 80,
        xy   = (350, 30),
    )

    add_text(
        draw = draw,
        text = "part 7",
        rtl  = False,
        size = 80,
        xy   = (350, 200),
    )


    add_text(
        draw = draw,
        text = "Mark Gardner          Gábor Szabó",
        rtl  = False,
        size = 80,
        xy   = (10, 420),
    )

    embed_image(img=img, filename='mark_gardner.png',   size=(200, 200), box=(10, 500))
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(200, 200), box=(width-200-10, 500))
    embed_image(img=img, filename='mojolicious.png', box=(10, 10), mask=True)

    img.save(png_filepath)
    img.show()


main()
