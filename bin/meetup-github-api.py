import os
from PIL import Image, ImageDraw, ImageFont
from mypil import heb, add_text, add_date, embed_image

width  = 1200
height = 675
isize = 200
background_color = '#eb8634'
#background_color = '#ebb434'
#background_color = '#f540dd'
#background_color = '#67f23d'
#background_color = '#DDDDDD'
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
        text = heb("שימוש ב API של גיטהב"),
        rtl  = True,
        xy   = (820, 30),
        size = 60,
    )

    add_text(
        draw = draw,
        text = "Using the REST and GraphQL",
        rtl  = False,
        xy   = (60, 160),
        size = 60,
    )

    add_text(
        draw = draw,
        text = "API of GitHub",
        rtl  = False,
        xy   = (60, 290),
        size = 60,
    )


    add_date(
        date_right = 630,
        date_top   = images_top,
        font       = font,
        draw       = draw,
        date       = "2023.05.07",
        day        = "יום א",
        hours      = "18:00-20:00",
    )


    add_text(
        draw = draw,
        text = heb("מרצה"),
        rtl  = True,
        xy   = (width - isize - 20, images_top),
        size = 30,
    )

    add_text(
        draw = draw,
        text = heb("גאבור סבו"),
        rtl  = True,
        xy   = (width - isize - 20, images_top + 50),
        size = 30,
    )

    embed_image(img=img, filename='gabor-2022-10-08-with-glasses-612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='code_maven_440x440.png', size=(isize, isize), box=(width-isize-10, 20), mask=True)
    #embed_image(img=img, filename='python.png', size=(isize, isize), box=(10, height-isize-10), mask=True)
    #embed_image(img=img, filename='gitlab.jpg', size=(isize, isize), box=(10, 20), mask=False)
    #embed_image(img=img, filename='docker.png', size=(isize, isize), box=(10, height-isize-10), mask=True)

    img.save(png_filepath)
    img.show()


main()
