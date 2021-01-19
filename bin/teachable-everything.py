import os
from PIL import Image, ImageDraw, ImageFont
from teachable import embed_image

width  = 1440
height = 780
background_color = '#fff'

root = os.path.dirname(os.path.dirname(__file__))
#print(root)

def main():
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    #print(png_filename)

    png_filepath = os.path.join(root, 'images', png_filename)
    #print(png_filepath)

    img = Image.new('RGB', (width, height), color=background_color)

    # Code-Maven Workshop

    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)


    embed_image(img=img, filename='golang.png',    size=(150, 150), box=(600, 600), mask=True)
    embed_image(img=img, filename='python.png',    size=(150, 150), box=(300, 600), mask=True)
    embed_image(img=img, filename='perl-left.png', size=(150, 150), box=(900, 600), mask=True)

    img.save(png_filepath)
    img.show()


main()
