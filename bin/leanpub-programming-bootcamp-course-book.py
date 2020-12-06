import os
from PIL import Image, ImageDraw, ImageFont
from mypil import add_text, add_date, embed_image

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

width  = 612
height = 792
background_color = '#eb8634'
#background_color = '#ebb434'

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
    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 90)
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 100)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
#    draw.text(
#        text="Programming Bootcamp for Scientists",
#        xy=(650, 130),
#        fill=(0, 0, 0),
#        font=font_title,
#    )
#
#    draw.text(
#        text="A Python course for people",
#        xy=(150, 530),
#        fill=(0, 0, 0),
#        font=font_title,
#    )
#    draw.text(
#        text="without programming background",
#        xy=(650, 630),
#        fill=(0, 0, 0),
#        font=font_title,
#    )
#
#    draw.text(
#        text="Learn and practice!",
#        xy=(70, 900),
#        fill=(0, 0, 0),
#        font=font_title,
#    )
#
#    draw.text(
#        text="Instructor",
#        xy=(1490, 1000),
#        fill=(0, 0, 0),
#        font=font_gabor,
#    )
    add_text(
        draw = draw,
        text = "Programming Bootcamp",
        rtl  = False,
        size = 50,
        xy   = (10, 180),
    )
    add_text(
        draw = draw,
        text = "for Scientists",
        rtl  = False,
        size = 50,
        xy   = (10, 270),
    )

    add_text(
        draw = draw,
        text = "Gábor Szabó",
        rtl  = False,
        size = 50,
        xy   = (110, 580),
    )


    isize = 500
    #embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-30, height-isize-30))
    embed_image(img=img, filename='python.png', box=(10, 0), mask=True)

    img.save(png_filepath)
    img.show()


main()
