import os
from PIL import Image, ImageDraw, ImageFont

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

def thumbnail(left, text, right=None):
    background_color = '#DDDDDD'

    width  = 960
    height = 540


    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    #print(png_filename)

    png_filepath = os.path.join(root, 'images', png_filename)
    #print(png_filepath)

    img = Image.new('RGB', (width, height), color=background_color)

    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 60)
    font_small = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    draw.text(
        text=text[0],
        xy=(210, 30),
        fill=(0, 0, 0),
        font=font,
    )
    draw.text(
        text=text[1],
        xy=(210, 130),
        fill=(0, 0, 0),
        font=font,
    )

    draw.text(
        text=text[2],
        xy=(50, 300),
        fill=(0, 0, 0),
        font=font_small,
    )

    draw.text(
        text=text[3],
        xy=(50, 370),
        fill=(0, 0, 0),
        font=font_small,
    )
    draw.text(
        text=text[4],
        xy=(50, 440),
        fill=(0, 0, 0),
        font=font_small,
    )


    embed_image(img=img, filename=left, size=(200, 200), box=(10, 10), mask=True)
    if right is not None:
        embed_image(img=img, filename=right, size=(200, 200), box=(width-200-10, 10), mask=True)


    img.save(png_filepath)
    img.show()


