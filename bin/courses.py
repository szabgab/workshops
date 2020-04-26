import os
from PIL import Image, ImageDraw, ImageFont

def rtl(txt):
    rev = txt[::-1]
    return rev


width  = 1200
height = 575
#background_color = '#eb8634'
background_color = '#ebb434'

root = os.path.dirname(os.path.dirname(__file__))
#print(root)

def embed_image(img, filename, box, size=None, mask=False):
    emb_img_path = os.path.join(root, 'src', filename)
    emb_img = Image.open(emb_img_path, 'r')
    #size = (emb_img.size[0] / 2, emb_img.size[1] / 2)
    if size:
        emb_img.thumbnail(size)
    if mask:
       img.paste(emb_img, box=box, mask=emb_img)
    else:
       img.paste(emb_img, box=box)

def add_course(draw, eng, heb, date, cnt):
    top = 20
    height = 130
    font_text = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 35)
    heb_width, heb_height = font_text.getsize(heb)
    draw.text(
        text = date,
        xy   = (50, top + cnt * height),
        fill = (0, 0, 0),
        font = font_text,
    )

    draw.text(
        text = eng,
        xy   = (300, top + cnt * height),
        fill = (0, 0, 0),
        font = font_text,
    )

    draw.text(
        text = rtl(heb),
        xy   = (1150-heb_width, top + cnt * height + 60),
        fill = (0, 0, 0),
        font = font_text,
    )



def main():
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    #print(png_filename)

    png_filepath = os.path.join(root, 'images', png_filename)
    #print(png_filepath)

    img = Image.new('RGB', (width, height), color=background_color)

    # Code-Maven Workshop

    font_text = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 80)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    draw.text(
        text="Code-Maven",
        xy=(150, 300),
        fill=(0, 0, 0),
        font=font_title,
    )

    add_course(
        draw = draw,
        eng  = "Docker for Developers and DevOps",
        heb  = "קורס דוקר למפתחים ולאנשי דבאופס",
        date = "2020.05.03",
        cnt  = 0,
    )

    add_course(
        draw = draw,
        eng  = "Testing in Python using Pytest",
        heb  = "קורס טסטינג בפייתון",
        date = "2020.05.17",
        cnt  = 1,
    )

    draw.text(
        text=rtl("מרצה:"),
        xy=(790, 400),
        fill=(0, 0, 0),
        font=font_gabor,
    )

    draw.text(
        text=rtl("גאבור סבו"),
        xy=(700, 450),
        fill=(0, 0, 0),
        font=font_gabor,
    )

    isize = 250
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
#    embed_image(img=img, filename='docker-moby-logo.png', box=(10, 10), mask=True)

    img.save(png_filepath)
    img.show()


main()
