import os
from PIL import Image, ImageDraw, ImageFont
from mypil import embed_image

width  = 1128
height = 191
#background_color = '#eb8634'
#background_color = '#ebb434'
background_color = '#b2ebf2'

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
#    draw.text(
#        text='Code-Maven',
#        xy=(10, 30),
#        fill=(0, 0, 0),
#        font=font_title,
#    )

    draw.text(
        text = 'Tips, ideas, tutorials',
        xy   = (170, 10),
        fill = (0, 0, 0),
        font = font_text,
    )
    draw.text(
        text  = 'about Python programming',
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
    embed_image(img=img, filename='python.png', size=(isize, isize), box=(30, height-isize-30), mask=True)

    img.save(png_filepath)
    img.show()


main()
