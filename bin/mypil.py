from PIL import Image, ImageDraw, ImageFont

def heb(txt):
    rev = txt[::-1]
    return rev

def add_text(draw, text, xy, size, rtl=False):
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', size)
    my_text = heb(text) if rtl else text
    width, height = font.getsize(my_text)
    new_xy = (xy[0]-width if rtl else xy[0], xy[1])
    draw.text(
        text = my_text,
        xy   = new_xy,
        fill = (0, 0, 0),
        font = font,
    )

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



