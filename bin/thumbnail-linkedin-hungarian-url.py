import os
from PIL import Image, ImageDraw, ImageFont
from mypil import add_text, add_date

width  = 1280
height = 720

# background_color = '#eb8634'
# background_color = '#ebb434'
background_color = '#CCC'

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
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 160)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)

    add_text(
        draw = draw,
        text = "Legyen neked is jó",
        rtl  = False,
        xy   = (30, 350),
        size = 90,
    )

    add_text(
        draw = draw,
        text = "LinkedIn címed!",
        rtl  = False,
        xy   = (30, 550),
        size = 90,
    )


    isize = 350
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    #embed_image(img=img, filename='python.png', box=(10, 10), mask=True)
    embed_image(img=img, filename='LinkedIn-In.png', size=(300, 300), box=(10, 10), mask=True)

    img.save(png_filepath)
    img.show()


main()
