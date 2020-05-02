import os
from PIL import Image, ImageDraw, ImageFont

width  = 1128
height = 191
#background_color = '#eb8634'
#background_color = '#ebb434'
background_color = '#b2ebf2'

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
    png_filepath = os.path.join(root, 'images', png_filename)

    img = Image.new('RGB', (width, height), color=background_color)

    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 80)
    font_text = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
#    draw.text(
#        text='Code-Maven',
#        xy=(10, 30),
#        fill=(0, 0, 0),
#        font=font_title,
#    )

    draw.text(
        text = 'Screencasts, interviews, articles',
        xy   = (10, 10),
        fill = (0, 0, 0),
        font = font_text,
    )
    draw.text(
        text  = 'about software development',
        xy    = (250, 70),
        fill  = (0, 0, 0),
        font  = font_text,
    )

    draw.text(
        text  = 'as seen by Gábor Szabó',
        xy    = (390, 130),
        fill  = (0, 0, 0),
        font  = font_text,
    )


    isize = 150
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-30, height-isize-30))

    img.save(png_filepath)
    img.show()


main()
