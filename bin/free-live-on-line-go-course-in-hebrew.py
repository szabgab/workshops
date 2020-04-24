import os
from PIL import Image, ImageDraw, ImageFont

def heb(txt):
    rev = txt[::-1]
    return rev

def add_date(date_right, date_top, font, draw, date, day, hours):
    date_width, date_height = font.getsize(date)
    draw.text(
        text=date,
        xy=(date_right-date_width, date_top),
        fill=(0, 0, 0),
        font=font,
    )
    day_width, day_height = font.getsize(day)
    draw.text(
        text=day,
        xy=(date_right-day_width, date_top+day_height+10),
        fill=(0, 0, 0),
        font=font,
    )
    hours_width, hours_height = font.getsize(hours)
    draw.text(
        text=hours,
        xy=(date_right-hours_width, date_top + day_height + hours_height + 25),
        fill=(0, 0, 0),
        font=font,
    )


width  = 1200
height = 675
#background_color = '#eb8634'
background_color = '#ebb434'
#background_color = '#f540dd'
#background_color = '#67f23d'

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
    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 60)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    draw.text(
        text="Code-Maven",
        xy=(250, 30),
        fill=(0, 0, 0),
        font=font_title,
    )

    draw.text(
        text = heb("קורס גו אונליין - פרק ו"),
        xy=(550, 130),
        fill=(0, 0, 0),
        font=font_title,
    )

    draw.text(
        text="Learn and practice the Go programming language.\n\nThis online event is in Hebrew.",
        xy=(70, 300),
        fill=(0, 0, 0),
        font=font_text,
    )


    add_date(
        date_right = 250,
        date_top   = 460,
        font       = font,
        draw       = draw,
        date       = "08.05.2020",
        day        = heb("יום ו"),
        hours      = "08:30-12:00",
    )

    hebrew = "מרצה:"
    draw.text(
        text=hebrew[::-1],
        xy=(790, 500),
        fill=(0, 0, 0),
        font=font_gabor,
    )

    hebrew = "גאבור סבו"
    draw.text(
        text=hebrew[::-1],
        xy=(700, 550),
        fill=(0, 0, 0),
        font=font_gabor,
    )

    isize = 250
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='golang.png', box=(10, 20), mask=True)

    img.save(png_filepath)
    img.show()


main()
