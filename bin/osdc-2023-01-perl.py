import os
import sys
from PIL import Image, ImageDraw, ImageFont
from mypil import add_text, add_date, embed_image

def heb(txt):
    rev = txt[::-1]
    return rev


width  = 1280
height = 720

# background_color = '#eb8634'
#background_color = '#ebb434'
background_color = '#DDDDDD'

root = os.path.dirname(os.path.dirname(__file__))
#print(root)

def main():
    if len(sys.argv) == 2:
        end = int(sys.argv[1])
    else:
        end = 1

    #for episode in ['1-1', '1-2']:
    #for episode in ['2-1', '2-2']:
    #for episode in ['3-1', '3-2']:
    #for episode in ['4-1', '4-2']:
    #for episode in ['5-1', '5-2']:
    #for episode in ['6-1', '6-2']:
    #for episode in ['7-1', '7-2']:
    #for episode in ['8-1', '8-2']:
    #for episode in ['9-1', '9-2']:
    #for episode in ['10-1', '10-2']:
    #for episode in ['11-1', '11-2']:
    #for episode in ['12-1']:
    for episode in ['13-1']:
        create_thumbnail(episode=episode, show=(end==1))


def create_thumbnail(episode, show=False):
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + f'_{episode}.png'
    #print(png_filename)

    img_dir = os.path.join(root, 'images', 'osdc')
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
        text = "OSDC 2023.01",
        rtl  = False,
        size = 80,
        xy   = (400, 30),
    )

    add_text(
        draw = draw,
        text = f"For Perl developers",
        rtl  = False,
        size = 80,
        xy   = (400, 140),
    )

    add_text(
        draw = draw,
        text = f"Part {episode}",
        rtl  = False,
        size = 80,
        xy   = (400, 250),
    )

    add_text(
        draw = draw,
        text = f"Open Source Development Course",
        rtl  = False,
        size = 70,
        xy   = (50, 450),
    )



    isize = 350
    fsize = 200
    #embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='code_maven_400x400.png', size=(isize, isize), box=(10, 10), mask=True)


    img.save(png_filepath)
    if show:
        img.show()


main()
