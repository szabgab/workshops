import os
import sys
from PIL import Image, ImageDraw, ImageFont
sys.path.append('bin')
from mypil import add_text, add_date, embed_image

def heb(txt):
    rev = txt[::-1]
    return rev


width  = 1128
height = 598

# background_color = '#eb8634'
#background_color = '#ebb434'
background_color = '#DDDDDD'

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#print(root)

def main():
    create_thumbnail(show=True)


def create_thumbnail(show=False):
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    #print(png_filename)

    img_dir = os.path.join(root, 'images')
    os.makedirs(img_dir, exist_ok=True)
    png_filepath = os.path.join(img_dir, png_filename)
    #print(png_filepath)

    img = Image.new('RGB', (width, height), color=background_color)

    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 160)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    add_text(
        draw = draw,
        text = "Gábor Szabó, trainer and mentor",
        rtl  = False,
        size = 70,
        xy   = (20, 20),
    )

    add_text(
        draw = draw,
        text = f"- Python (beginner, advanced, testing, web)",
        rtl  = False,
        size = 50,
        xy   = (20, 180),
    )

    add_text(
        draw = draw,
        text = f"- Git, GitHub, GitLab",
        rtl  = False,
        size = 50,
        xy   = (20, 250),
    )

    add_text(
        draw = draw,
        text = f"- Docker",
        rtl  = False,
        size = 50,
        xy   = (20, 320),
    )

    add_text(
        draw = draw,
        text = f"Training courses by Gábor Szabó",
        rtl  = False,
        size = 35,
        xy   = (280, height-120),
    )


    embed_image(img=img, filename='gabor-2022-10-08-with-glasses-612x612.jpg', size=(200, 200), box=(width-200-10, height-200-10))
    embed_image(img=img, filename='code_maven_400x400.png', size=(200, 200), box=(10, height-200-10), mask=True)


    img.save(png_filepath)
    if show:
        img.show()


main()
