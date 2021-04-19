import os
from PIL import Image, ImageDraw, ImageFont
from mypil import heb, add_text, add_date, embed_image

width  = 1200
height = 675
isize = 200
#background_color = '#eb8634'
#background_color = '#ebb434'
#background_color = '#f540dd'
#background_color = '#67f23d'
background_color = '#DDDDDD'
images_top = height - isize - 10

root = os.path.dirname(os.path.dirname(__file__))
#print(root)

def main():
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    #print(png_filename)

    png_filepath = os.path.join(root, 'images', png_filename)
    #print(png_filepath)

    img = Image.new('RGB', (width, height), color=background_color)

    # Code-Maven Workshop

    font_text = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 60)
    font_title2 = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 55)
    font_subtitle = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)

    add_text(
        draw = draw,
        text = "Live coding cucumber-playwright",
        rtl  = False,
        xy   = (20, 30),
        size = 60,
    )

    add_text(
        draw = draw,
        text = "in TypeScript with Tally Barak",
        rtl  = False,
        xy   = (20, 140),
        size = 60,
    )

#    add_text(
#        draw = draw,
#        text = "with Tally Barak",
#        rtl  = False,
#        xy   = (20, 250),
#        size = 60,
#    )

#    add_text(
#        draw = draw,
#        text = "(in English)",
#        rtl  = False,
#        xy   = (20, 360),
#        size = 60,
#    )


    add_date(
        date_right = 690,
        date_top   = images_top,
        font       = font,
        draw       = draw,
        date       = "2021.04.18",
        day        = "Sunday",
        hours      = "14:00-16:00",
    )

    add_text(
        draw = draw,
        text = "Tally Barak",
        rtl  = False,
        xy   = (40, 400),
        size = 30,
    )


#    add_text(
#        draw = draw,
#        text = "מרצה",
#        rtl  = True,
#        xy   = (width - isize - 20, images_top),
#        size = 30,
#    )
#
    add_text(
        draw = draw,
        text = "Gábor Szabó",
        rtl  = False,
        xy   = (980, 400),
        size = 30,
    )

    #embed_image(img=img, filename='rex.png', box=(10, 10), mask=True)
    embed_image(img=img, filename='tally_barak.png', size=(isize, isize), box=(10, height-isize-10))
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='code_maven_440x440.png', size=(isize, isize), box=(width-isize-10, 20), mask=True)
    #embed_image(img=img, filename='python.png', size=(isize, isize), box=(10, height-isize-10), mask=True)
    #embed_image(img=img, filename='gitlab.jpg', size=(isize, isize), box=(10, 20), mask=False)
    #embed_image(img=img, filename='docker.png', size=(isize, isize), box=(10, height-isize-10), mask=True)

    img.save(png_filepath)
    img.show()


main()
