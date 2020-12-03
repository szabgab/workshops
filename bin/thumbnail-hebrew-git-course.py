import os
import sys
from PIL import Image, ImageDraw, ImageFont
from mypil import add_text, add_date, embed_image


width  = 1280
height = 720

# background_color = '#eb8634'
#background_color = '#ebb434'
background_color = '#FFF'

root = os.path.dirname(os.path.dirname(__file__))
#print(root)

def main():
    if len(sys.argv) == 2:
        end = int(sys.argv[1])
    else:
        end = 1

    for episode in range(1, end+1):
        create_thumbnail(episode=episode, show=(end==1))


def create_thumbnail(episode, show=False):
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + f'_{episode:02n}.png'
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
        text = "קורס גיט",
        rtl  = True,
        size = 80,
        xy   = (1050, 30),
    )

    add_text(
        draw = draw,
        text = f"פרק",
        rtl  = True,
        size = 80,
        xy   = (1050, 140),
    )

    add_text(
        draw = draw,
        text = str(episode),
        rtl  = False,
        size = 80,
        xy   = (750, 140),
    )


    isize = 350
    fsize = 200
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='git-logo-512x214.png', size=(isize, isize), box=(10, 10), mask=True)
    embed_image(img=img, filename='github-octocat.png', size=(isize, isize), box=(10, 400), mask=True)
    embed_image(img=img, filename='gitlab.jpg', size=(isize, isize), box=(400, 400), mask=False)


    img.save(png_filepath)
    if show:
        img.show()


main()
