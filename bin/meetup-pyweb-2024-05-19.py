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
#background_color = '#DDDDDD'
background_color = '#FFFFFF'
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
    #draw.text(
    #    text="Storemaven - Code-Maven",
    #    xy=(230, 30),
    #    fill=(0, 0, 0),
    #    font=font_title,
    #)

    add_text(
        draw = draw,
        text = "PyWeb - Python in Israel Meetup",
        rtl  = False,
        xy   = (200, 30),
        size = 60,
    )

#    add_text(
#        draw = draw,
#        text = "",
#        rtl  = False,
#        xy   = (280, 160),
#        size = 60,
#    )
#
#    add_text(
#        draw = draw,
#        text = "",
#        rtl  = False,
#        xy   = (200, 250),
#        size = 55,
#    )
#    add_text(
#        draw = draw,
#        text = "",
#        rtl  = False,
#        xy   = (200, 300),
#        size = 55,
#    )

#    add_text(
#        draw = draw,
#        text = "+ 1 presentation",
#        rtl  = False,
#        xy   = (20, 380),
#        size = 55,
#    )



    add_date(
        date_right = 430,
        date_top   = images_top,
        font       = font,
        draw       = draw,
        date       = "May 19, 2024",
        day        = "18:00-20:00",
        hours      = "ZenCity, Tel Aviv",
    )


#    add_text(
#        draw = draw,
#        text = "מרצה",
#        rtl  = True,
#        xy   = (width - isize - 20, images_top),
#        size = 30,
#    )
#
#    add_text(
#        draw = draw,
#        text = "גאבור סבו",
#        rtl  = True,
#        xy   = (width - isize - 20, images_top + 50),
#        size = 30,
#    )

    #embed_image(img=img, filename='israel-flag-small.png', size=(isize, isize), box=(width-isize-10, 10))
    #embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    #embed_image(img=img, filename='code_maven_440x440.png', size=(isize, isize), box=(width-isize-10, 20), mask=True)
    embed_image(img=img, filename='python.png', size=(isize, isize), box=(10, 10), mask=True)
    embed_image(img=img, filename='zencity_logo_dark.jpg', size=(600, 313), box=(500, height-344-30), mask=False)

    img.save(png_filepath)
    img.show()


main()
