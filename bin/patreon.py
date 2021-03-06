import os
from PIL import Image, ImageDraw, ImageFont
from mypil import embed_image, add_text

width  = 1600
height = 400
background_color = '#ffffff'

root = os.path.dirname(os.path.dirname(__file__))
#print(root)

def main():
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    png_filepath = os.path.join(root, 'images', png_filename)

    img = Image.new('RGB', (width, height), color=background_color)

    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 80)
    font_text = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)

    add_text(
        draw = draw,
        text = 'Code       Maven',
        rtl  = False,
        xy   = ('center', 30),
        size = 60,
    )
    add_text(
        draw = draw,
        #text = 'screencasts, blog posts, code-snippets',
        text = 'Helping developers create better software',
        rtl  = False,
        xy   = ('center', 120),
        size = 40,
    )


    add_text(
        draw = draw,
        text = 'Test Automation - Continuous Integration - DevOps',
        rtl  = False,
        xy   = ('center', 200),
        size = 40,
    )


    isize = 150
    embed_image(img=img, filename='code_maven_440x440.png', size=(70, 70), box=(745, 23), mask=True)
    embed_image(img=img, filename='perl.png', size=(isize, isize), box=(30, 30), mask=True)
    embed_image(img=img, filename='tessa.png', size=(isize, isize), box=(width-isize-30, 30), mask=True)
    #embed_image(img=img, filename='golang.png', size=(isize, isize), box=(width-isize-30, 30), mask=True)
    embed_image(img=img, filename='tux.png', size=(isize, isize), box=(width-isize-30, height-isize-30), mask=True)
    embed_image(img=img, filename='docker-moby-logo.png', size=(isize, isize), box=(30, height-isize-30), mask=True)

    img.save(png_filepath)
    img.show()


main()
