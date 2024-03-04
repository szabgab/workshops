import os
from PIL import Image, ImageDraw, ImageFont
from mypil import add_text, add_date, embed_image, heb

width  = 1280
height = 720

#background_color = '#eb8634'
#background_color = '#ebb434'
# background_color = '#DDDDDD'
background_color = "#59D5E0"
#background_color = "#3ea3c1"

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
        text = heb("קורס ראסט - פרק 7"),
        rtl  = True,
        size = 65,
        xy   = (1250, 30),
    )

    add_text(
        draw = draw,
        #text = heb("מתחילים לתכנת בראסט"),
        #text = heb("קפיצה קצרה לקליפי"),
        #text = heb("המרת מחרוזת למספר"),
        #text = heb("פרמטרים בשורת הפקודה"),
        #text = heb("חמישה שיפורים"),
        #text = heb("מספרים וטיפוסים"),
        text = heb("פונקציה וטסטים"),
        rtl  = True,
        size = 65,
        xy   = (1250, 180),
    )

    add_text(
        draw = draw,
        text = "Rust Course - part 7",
        rtl  = False,
        size = 64,
        xy   = (20, 420),
    )

    add_text(
        draw = draw,
        #text = "Start learning Rust",
        #text = "A short jump to Clippy",
        #text = "Convert a string to a number",
        #text = "Command line parameters - args",
        #text = "Turbofish, use, -q, fmt, absolute_paths",
        #text = "Numbers and types of numbers",
        text = "Function and testing",
        rtl  = False,
        size = 65,
        xy   = (20, 580),
    )


    isize = 350
    #embed_image(img=img, filename='gabor2_612x612.jpg', size=(isize, isize), box=(width-isize-10, height-isize-10))
    embed_image(img=img, filename='rust-logo-512x512.png', size=(isize, isize), box=(10, 10), mask=True)
    #embed_image(img=img, filename='code_maven_440x440.png', size=(isize, isize), box=(width-isize-10, 360), mask=True)


    img.save(png_filepath)
    img.show()


main()