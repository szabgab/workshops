import os
from PIL import Image, ImageDraw, ImageFont


width  = 1200
height = 675
root = os.path.dirname(os.path.dirname(__file__))
#print(root)

def embed_image(img, filename, box, mask=False):
    emb_img_path = os.path.join(root, 'src', filename)
    emb_img = Image.open(emb_img_path, 'r')
    size = (emb_img.size[0] / 2, emb_img.size[1] / 2)
    emb_img.thumbnail(size)
    if mask:
       img.paste(emb_img, box=box, mask=emb_img)
    else:
       img.paste(emb_img, box=box)

def main():
    png_filename = os.path.splitext(os.path.basename(__file__))[0] + '.png'
    #print(png_filename)

    png_filepath = os.path.join(root, 'images', png_filename)
    #print(png_filepath)

    # also nice: #eb8634
    img = Image.new('RGB', (width, height), color='#ebb434')

    #font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
    font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 40)
    draw = ImageDraw.Draw(img)
    draw.text(
        text="Recursion vs. Iteration in Python",
        xy=(10, 10),
        fill=(0, 0, 0),
        font=font,
    )

    hebrew_title = "רקורסיה או איטרציה בפיתון"
    draw.text(
        text=hebrew_title[::-1],
        xy=(50, 70),
        fill=(0, 0, 0),
        font=font,
    )

    embed_image(img=img, filename='gabor2_612x612.jpg', box=(50, 50))
    embed_image(img=img, filename='python.png', box=(10, 10), mask=True)

    #img.save(png_filepath)
    img.show()


main()