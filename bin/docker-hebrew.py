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

    create_thumbnail(show=(end==1))


def create_thumbnail(show=False):
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + f'.png'
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
        text = heb("קורס דוקר"),
        rtl  = True,
        size = 80,
        xy   = (1250, 30),
    )

    add_text(
        draw = draw,
#        text = heb(f"למה להשתמש בדוקר?"),
#        text = heb(f"מה זה דוקר?"),
#        text = heb(f"ימיגיז וקונטיינרים"),
#        text = heb(f"התקנת דוקר"),
#        text = heb(f"המנוע של דוקר"),
#        text = heb(f"דוקר רגיסטרי"),
        text = heb(f"שלום עולם עם דוקר"),
        rtl  = True,
        size = 80,
        xy   = (1250, 140),
    )

#    add_text(
#        draw = draw,
#        text = heb(f"פרק {episode}"),
#        rtl  = True,
#        size = 80,
#        xy   = (1250, 240),
#    )

#    add_text(
#        draw = draw,
#        text = "An introduction to Python",
#        rtl  = False,
#        size = 80,
#        xy   = (100, 250),
#    )

    add_text(
        draw = draw,
        text = f"Docker Course",
        rtl  = False,
        size = 70,
        xy   = (50, 450),
    )

    add_text(
        draw = draw,
#        text = f"Why use Docker?",
#        text = f"What is Docker?",
#        text = f"Images vs. containers",
#        text = f"Installing Docker",
#        text = f"Desktop - Engine - Client",
#        text = f"Docker Registry",
        text = f"Hello World! in Docker",
        rtl  = False,
        size = 70,
        xy   = (50, 560),
    )

    isize = 350
    fsize = 200
    #embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='docker-moby-logo.png', size=(300, 300), box=(20, 20), mask=True)
    embed_image(img=img, filename='code_maven_400x400.png', size=(300, 300), box=(960, 430), mask=True)


    img.save(png_filepath)
    if show:
        img.show()


main()
