import os
from PIL import Image, ImageDraw, ImageFont

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
        xy=(date_right-day_width, date_top+day_height),
        fill=(0, 0, 0),
        font=font,
    )
    hours_width, hours_height = font.getsize(hours)
    draw.text(
        text=hours,
        xy=(date_right-hours_width, date_top + day_height + hours_height + 5),
        fill=(0, 0, 0),
        font=font,
    )


width  = 1200
height = 675
# background_color = '#eb8634'
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
        xy=(220, 30),
        fill=(0, 0, 0),
        font=font_title,
    )

    draw.text(
        text="Online Office Hours in Hebrew",
        xy=(220, 110),
        fill=(0, 0, 0),
        font=font_title,
    )

    draw.text(
        text="Beating the chicken-egg problem:\nHow to gain experience before getting a job?\n\nThis online event is in Hebrew.",
        #text="Beating the chicken-egg problem:\nHow to gain experience before getting a job?\n\n- Python Programmer\n- Test/QA Automation Engineer\n- DevOps Engineer",
        xy=(70, 250),
        fill=(0, 0, 0),
        font=font_text,
    )


    add_date(
        date_right = 250,
        date_top   = 440,
        font       = font,
        draw       = draw,
        date       = "12.03.2020",
        day        = "יום ה"[::-1],
        hours      = "19:30-20:30",
    )

    hebrew = "גאבור סבו"
    draw.text(
        text=hebrew[::-1],
        xy=(700, 500),
        fill=(0, 0, 0),
        font=font_gabor,
    )

    isize = 250
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='python.png', box=(10, 10), mask=True)

    img.save(png_filepath)
    img.show()


main()
