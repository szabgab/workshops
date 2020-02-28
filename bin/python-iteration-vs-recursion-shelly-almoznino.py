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

    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 30)
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

    draw.text(
        text="12.03.2020",
        xy=(110, 240),
        fill=(0, 0, 0),
        font=font,
    )
    draw.text(
        text="יום ה"[::-1],
        xy=(160, 280),
        fill=(0, 0, 0),
        font=font,
    )
    draw.text(
        text="17:30-21:30",
        xy=(110, 320),
        fill=(0, 0, 0),
        font=font,
    )

    hebrew = "מרצה אורחת"
    draw.text(
        text=hebrew[::-1],
        xy=(350, 400),
        fill=(0, 0, 0),
        font=font,
    )
    hebrew = "שלי אלמוזנינו"
    draw.text(
        text=hebrew[::-1],
        xy=(350, 500),
        fill=(0, 0, 0),
        font=font,
    )

    hebrew = "תל אביב"
    draw.text(
        text=hebrew[::-1],
        xy=(750, 500),
        fill=(0, 0, 0),
        font=font,
    )
    hebrew = "גוגל קמפוס"
    draw.text(
        text=hebrew[::-1],
        xy=(750, 540),
        fill=(0, 0, 0),
        font=font,
    )

    hebrew = "מנחה: גאבור סבו"
    draw.text(
        text=hebrew[::-1],
        xy=(700, 620),
        fill=(0, 0, 0),
        font=font_gabor,
    )

    isize = 250
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='shelly_almoznino.jpg', size=(isize, isize), box=(10, height-isize-10))
    embed_image(img=img, filename='python.png', box=(10, 10), mask=True)

    #img.save(png_filepath)
    img.show()


main()