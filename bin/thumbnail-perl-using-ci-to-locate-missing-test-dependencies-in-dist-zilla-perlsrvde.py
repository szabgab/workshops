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
        text = "Using GitHub Actions (CI)",
        rtl  = False,
        size = 65,
        xy   = (250, 30),
    )

    add_text(
        draw = draw,
        text = "to locate missing dependencies",
        rtl  = False,
        size = 65,
        xy   = (250, 220),
    )

    add_text(
        draw = draw,
        text = "in a Perl project",
        rtl  = False,
        size = 65,
        xy   = (250, 400),
    )

#    add_text(
#        draw = draw,
#        text = "   dependencies",
#        rtl  = False,
#        size = 80,
#        xy   = (250, 580),
#    )

    #add_text(
    #    draw = draw,
    #    text = "14 minutes",
    #    rtl  = False,
    #    size = 60,
    #    xy   = (250, 540),
    #)


    isize = 350
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='perl-left.png',      size=(200, 200),     box=(10, 10),     mask=True)

    img.save(png_filepath)
    img.show()


main()
