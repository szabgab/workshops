import os
from PIL import Image, ImageDraw, ImageFont
from mypil import heb, add_text, add_date, embed_image

width  = 1280
height = 720

# background_color = '#eb8634'
# background_color = '#ebb434'
background_color = '#EEEEEE'

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
        text = "LinkedIn connections",
        rtl  = False,
        xy   = (10, 350),
        size = 70,
    )


    add_text(
        draw = draw,
        text = "קשרים בלינקדין",
        rtl  = True,
        xy   = (900, 500),
        size = 70,
    )

#    add_text(
#        draw = draw,
#        text = "איך משתמשים בסלאק?",
#        rtl  = True,
#        xy   = (1200, 130),
#        size = 60,
#    )


    isize = 200 
    embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    #embed_image(img=img, filename='python.png', box=(10, 10), mask=True)
    embed_image(img=img, filename='LI-In-Bug.png', size=(300, 300), box=(10, 10), mask=True)
    embed_image(img=img, filename='danit-raanan.jpeg', box=(10, height-isize-10))

    img.save(png_filepath)
    img.show()


main()
