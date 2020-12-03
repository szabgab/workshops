import os
from PIL import Image, ImageDraw, ImageFont
from mypil import heb, add_text, add_date

width  = 1200
height = 675
isize = 200
#background_color = '#eb8634'
background_color = '#ebb434'
#background_color = '#f540dd'
#background_color = '#67f23d'
images_top = height - isize - 10

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
    font_title2 = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 55)
    font_subtitle = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    draw.text(
        text="Code-Maven      -   LinkedIn",
        xy=(250, 30),
        fill=(0, 0, 0),
        font=font_title,
    )

    add_text(
        draw = draw,
        text = "מציאת עבודה )חדשה( בהיי-טק",
        rtl  = True,
        xy   = (1100, 130),
        size = 60,
    )

    add_text(
        draw = draw,
        text = "שיחה עם דנית רענן אידסס",
        rtl  = True,
        xy   = (1100, 230),
        size = 60,
    )

    add_text(
        draw = draw,
        text = "מגייסת ואשת כח אדם",
        rtl  = True,
        xy   = (1100, 330),
        size = 60,
    )

    add_date(
        date_right = 730,
        date_top   = images_top,
        font       = font,
        draw       = draw,
        date       = "03.06.2020",
        day        = heb("יום ד"),
        hours      = "09:00-10:00",
    )


    add_text(
        draw = draw,
        text = "מארח",
        rtl  = True,
        xy   = (width - isize - 20, images_top),
        size = 30,
    )

    add_text(
        draw = draw,
        text = "גאבור סבו",
        rtl  = True,
        xy   = (width - isize - 20, images_top + 50),
        size = 30,
    )

    add_text(
        draw = draw,
        text = "אורחת",
        rtl  = True,
        xy   = (445, images_top),
        size = 30,
    )

    add_text(
        draw = draw,
        text = "דנית רענן אידסס",
        rtl  =  True,
        xy   = (445, images_top + 50),
        size = 30,
    )

    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='LinkedIn-In.png', size=(isize, isize), box=(10, 20), mask=True)
    embed_image(img=img, filename='danit-raanan.jpeg', size=(isize, isize), box=(10, height-isize-10))

    img.save(png_filepath)
    img.show()


main()
