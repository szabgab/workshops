import os
from PIL import Image, ImageDraw, ImageFont
from mypil import add_text, add_date, embed_image, heb

width  = 1280
height = 720

background_color = '#eb8634'
#background_color = '#ebb434'
# background_color = '#DDDDDD'

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
        text = "Python Programming course",
        rtl  = False,
        size = 80,
        xy   = (50, 50),
    )

    add_text(
        draw = draw,
        text = "Weizmann Institute - 3-3 (part 9)",
        rtl  = False,
        size = 80,
        xy   = (50, 150),
    )


    add_text(
        draw = draw,
        #text = "__pycache__, .gitignore",
        text = "count digits of a string",
        rtl  = False,
        size = 80,
        xy   = (50, 300),
    )


    add_text(
        draw = draw,
#        text = "About GitHub, Programming",
#        text = "GitHub Pages via GitHub UI",
#        text = "Installing git on Windows",
#        text = "Installing VS Code and Python",
#        text = "Getting input from STDIN",
#        text = "flow control in Python",
#        text = "Git, code-formatting, random.py",
        text = "Python lists",
        rtl  = False,
        size = 80,
        xy   = (50, 420),
    )

#    add_text(
#        draw = draw,
#        text = "split code into functions",
#        rtl  = False,
#        size = 80,
#        xy   = (50, 540),
#    )


    #isize = 350
    #embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    #embed_image(img=img, filename='rust-logo-512x512.png', size=(isize, isize), box=(10, 10), mask=True)
    #embed_image(img=img, filename='code_maven_440x440.png', size=(isize, isize), box=(width-isize-10, 360), mask=True)


    img.save(png_filepath)
    img.show()


main()
