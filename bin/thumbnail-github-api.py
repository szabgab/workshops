import os
from PIL import Image, ImageDraw, ImageFont
from mypil import add_text, add_date, embed_image, heb

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
        text = heb("אפי של גיטהב"),
        rtl  = True,
        size = 80,
        xy   = (850, 30),
    )

#    add_text(
#        draw = draw,
#        text = heb("בעזרת גיטהב אקשינס"),
#        rtl  = True,
#        size = 80,
#        xy   = (850, 130),
#    )

    add_text(
        draw = draw,
        text = heb("פרק ב"),
        rtl  = True,
        size = 80,
        xy   = (850, 230),
    )


    add_text(
        draw = draw,
        text = "Using the GraphQL",
        rtl  = False,
        size = 80,
        xy   = (50, 400),
    )

    add_text(
        draw = draw,
        text = "API of GitHub",
        rtl  = False,
        size = 80,
        xy   = (50, 500),
    )

    add_text(
        draw = draw,
        text = "Part 2",
        rtl  = False,
        size = 80,
        xy   = (50, 600),
    )


    isize = 350
    fsize = 200
    embed_image(img=img, filename='gabor-2022-10-08-with-glasses-612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='code_maven_440x440.png', size=(isize, isize), box=(width-isize-10, 20), mask=True)
    #embed_image(img=img, filename='github-octocat.png', size=(isize, isize), box=(10, 400), mask=True)
#    embed_image(img=img, filename='israel-flag-small.png', size=(fsize, fsize), box=(width-fsize-10, height-isize-fsize+30), mask=False)


    img.save(png_filepath)
    img.show()


main()
