import os
from PIL import Image, ImageDraw, ImageFont
from mypil import add_text, add_date, embed_image

width  = 1280
height = 720

# background_color = '#eb8634'
#background_color = '#ebb434'
background_color = '#DDDDDD'

root = os.path.dirname(os.path.dirname(__file__))
#print(root)

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
        text = "Continuous Integration (CI)",
        rtl  = False,
        size = 80,
        xy   = (30, 30),
    )

    add_text(
        draw = draw,
        text = "for every Perl module on CPAN",
        rtl  = False,
        size = 80,
        xy   = (30, 220),
    )

    add_text(
        draw = draw,
        text = "What is CI?",
        rtl  = False,
        size = 80,
        xy   = (30, 400),
    )

    add_text(
        draw = draw,
        text = "Why is it good for you?",
        rtl  = False,
        size = 80,
        xy   = (30, 580),
    )

    #add_text(
    #    draw = draw,
    #    text = "14 minutes",
    #    rtl  = False,
    #    size = 60,
    #    xy   = (250, 540),
    #)


    isize = 350
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    #embed_image(img=img, filename='metacpan.jpg', box=(10, 10), mask=False)

    img.save(png_filepath)
    img.show()


main()
