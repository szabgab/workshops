import os
from PIL import Image, ImageDraw, ImageFont

def heb(txt):
    rev = txt[::-1]
    return rev


def add_dates(date_right, date_top, font, draw, dates):
    for i, this in enumerate(dates):
        date_width, date_height = font.getsize(this['date'])
        day_width, day_height = font.getsize(this['day'])

        draw.text(
            text = this['date'],
            xy   = (date_right-date_width, date_top),
            fill = (0, 0, 0),
            font = font,
        )
        draw.text(
            text = this['day'],
            xy   = (date_right-date_width-day_width-30, date_top),
            fill = (0, 0, 0),
            font = font,
        )
        date_top += date_height + 20

width  = 1440
height = 780
#background_color = '#eb8634'
#background_color = '#ebb434'
background_color = '#2fa149'

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

def main():
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    #print(png_filename)

    png_filepath = os.path.join(root, 'images', png_filename)
    #print(png_filepath)

    img = Image.new('RGB', (width, height), color=background_color)

    # Code-Maven Workshop

    font_text = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 90)
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 90)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
#    draw.text(
#        text="Functional Programming",
#        xy=(250, 130),
#        fill=(0, 0, 0),
#        font=font_title,
#    )
#
#    draw.text(
#        text="with Python",
#        xy=(250, 270),
#        fill=(0, 0, 0),
#        font=font_title,
#    )
#    draw.text(
#        text="without programming background",
#        xy=(650, 630),
#        fill=(0, 0, 0),
#        font=font_title,
#    )


#    draw.text(
#        text = heb("קורס דוקר למפתחים ולאנשי דבאופס"),
#        xy   =(550, 330),
#        fill =(0, 0, 0),
#        font =font_title,
#    )


    draw.text(
        text="Learn and practice!",
        xy=(70, 900),
        fill=(0, 0, 0),
        font=font_title,
    )

    draw.text(
        text="Instructor",
        xy=(1490, 1000),
        fill=(0, 0, 0),
        font=font_gabor,
    )

    draw.text(
        text="Gábor Szabó",
        xy=(1360, 1100),
        fill=(0, 0, 0),
        font=font_gabor,
    )

    isize = 300
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-30, height-isize-30))
    embed_image(img=img, filename='python.png', box=(30, 30), mask=True)

    img.save(png_filepath)
    img.show()


main()
