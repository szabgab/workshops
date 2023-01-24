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

    font_gabor = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font_title = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 160)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    add_text(
        draw = draw,
        text = "Kantoniko #5",
        rtl  = False,
        size = 80,
        xy   = (420, 80),
    )

    add_text(
        draw = draw,
        text = "Ladino phrases, games",
        rtl  = False,
        size = 80,
        xy   = (50, 250),
    )
 
    add_text(
        draw = draw,
        text = "Spanish stories by Buly Hazan",
        rtl  = False,
        size = 80,
        xy   = (50, 380),
    )


    add_text(
        draw = draw,
        text = "English and Hebrew info",
        rtl  = False,
        size = 80,
        xy   = (50, 510),
    )

#    add_text(
#        draw = draw,
#        text = "- JavaScript",
#        rtl  = False,
#        size = 50,
#        xy   = (250, 350),
#    )

#    add_text(
#        draw = draw,
#        text = "- Bulma",
#        rtl  = False,
#        size = 50,
#        xy   = (250, 430),
#    )
#
#    add_text(
#        draw = draw,
#        text = "- GitHub actions and pages",
#        rtl  = False,
#        size = 50,
#        xy   = (250, 510),
#    )



#    add_text(
#        draw = draw,
#        text = "2022.05.17   18:00          Gábor Szabó",
#        rtl  = False,
#        size = 60,
#        xy   = (10, 620),
#    )

    embed_image(img=img, filename='gabor2_612x612.jpg', size=(200, 200), box=(width-200-10, 500))
    embed_image(img=img, filename='sephardic-flag.png', size=(300, 300), box=(10, 10), mask=True)

    img.save(png_filepath)
    img.show()


main()
