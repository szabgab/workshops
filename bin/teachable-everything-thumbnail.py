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

width  = 960
height = 540
background_color = '#fff'

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
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 70)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    draw.text(
        text="The Everything Bundle",
        xy=(180, 40),
        fill=(0, 0, 0),
        font=font_title,
    )

    draw.text(
        text="All the",
        xy=(220, 200),
        fill=(0, 0, 0),
        font=font_title,
    )
    draw.text(
        text="Perl, Python, and Go",
        xy=(220, 300),
        fill=(0, 0, 0),
        font=font_title,
    )
    draw.text(
        text="courses",
        xy=(220, 400),
        fill=(0, 0, 0),
        font=font_title,
    )


    isize = 300
    embed_image(img=img, filename='perl.png',     size=(150, 150), box=(30, 30),  mask=True)
    embed_image(img=img, filename='golang.png',   size=(150, 150), box=(30, 200), mask=True)
    embed_image(img=img, filename='python.png',   size=(150, 150), box=(30, 370), mask=True)

    img.save(png_filepath)
    img.show()


main()
