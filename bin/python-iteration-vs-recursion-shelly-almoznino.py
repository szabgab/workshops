import os
from PIL import Image, ImageDraw, ImageFont


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

    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 60)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    draw.text(
        text="Recursion vs. Iteration in Python",
        xy=(220, 30),
        fill=(0, 0, 0),
        font=font_title,
    )

    hebrew_title = "רקורסיה או איטרציה בפיתון"
    draw.text(
        text=hebrew_title[::-1],
        xy=(320, 120),
        fill=(0, 0, 0),
        font=font_title,
    )

    date_right =  500
    date = "12.03.2020"
    date_width, date_height = font.getsize(date)
    draw.text(
        text=date,
        xy=(date_right-date_width, 240),
        fill=(0, 0, 0),
        font=font,
    )
    day = "יום ה"[::-1]
    day_width, day_height = font.getsize(day)
    draw.text(
        text=day,
        xy=(date_right-day_width, 280),
        fill=(0, 0, 0),
        font=font,
    )
    hours = "17:30-21:30"
    hours_width, hours_height = font.getsize(hours)
    draw.text(
        text=hours,
        xy=(date_right-hours_width, 320),
        fill=(0, 0, 0),
        font=font,
    )

    speaker_right = 550
    hebrew_speaker = "מרצה אורחת"
    hebrew_speaker_width, hebrew_speaker_height = font.getsize(hebrew_speaker)
    draw.text(
        text=hebrew_speaker[::-1],
        xy=(speaker_right-hebrew_speaker_width, 450),
        fill=(0, 0, 0),
        font=font,
    )

    speaker_name = "שלי אלמוזנינו"
    speaker_name_width, speaker__name_height = font.getsize(speaker_name)
    draw.text(
        text=speaker_name[::-1],
        xy=(speaker_right-speaker_name_width, 500),
        fill=(0, 0, 0),
        font=font,
    )

    hebrew = "תל אביב"
    draw.text(
        text=hebrew[::-1],
        xy=(750, 250),
        fill=(0, 0, 0),
        font=font,
    )
    hebrew = "גוגל קמפוס"
    draw.text(
        text=hebrew[::-1],
        xy=(750, 300),
        fill=(0, 0, 0),
        font=font,
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
    embed_image(img=img, filename='shelly_almoznino.jpg', size=(isize, isize), box=(10, height-isize-10))
    embed_image(img=img, filename='python.png', box=(10, 10), mask=True)

    img.save(png_filepath)
    img.show()


main()