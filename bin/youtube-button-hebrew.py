import os
from PIL import Image, ImageDraw, ImageFont
from mypil import heb, add_text, add_date

width  = 350
height = 350

# background_color = '#eb8634'
# background_color = '#ebb434'
background_color = '#FFFFFF'

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
        text = "מביני קוד",
        rtl  = True,
        xy   = (330, 70),
        size = 70,
        fill = (0, 0, 255),
    )

    add_text(
        draw = draw,
        text = "עקוב אחרי",
        rtl  = True,
        xy   = (340, 170),
        size = 70,
        fill = (0, 0, 255),
    )

#    add_text(
#        draw = draw,
#        text = "איך משתמשים בסלאק?",
#        rtl  = True,
#        xy   = (1200, 130),
#        size = 60,
#    )


    isize = 350
    #embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    #embed_image(img=img, filename='python.png', box=(10, 10), mask=True)
    #embed_image(img=img, filename='LinkedIn-In.png', size=(300, 300), box=(10, 10), mask=True)

    img.save(png_filepath)
    img.show()


main()
