import os
from PIL import Image, ImageDraw, ImageFont

def heb(txt):
    rev = txt[::-1]
    return rev


width  = 312
height = 312

#background_color = '#eb8634'
#background_color = '#ebb434'
background_color = '#eeeeee'

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

    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 60)
    draw = ImageDraw.Draw(img)

    draw.text(
        text  = heb("מביני קוד"),
        xy    = (20, 60),
        fill  = (0, 0, 0),
        font  = font_title,
    )
    draw.text(
        text  = heb("מביני קוד"),
        xy    = (20, 60),
        fill  = (0, 0, 0),
        font  = font_title,
    )


    img.save(png_filepath)
    img.show()


main()
