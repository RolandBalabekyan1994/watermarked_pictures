from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import glob



def copyright_apply(Source_images, Output_images, text):
    photo = Image.open(Source_images)

    w, h = photo.size

    drawing = ImageDraw.Draw(photo)
    black = (3, 8, 12)
    font = ImageFont.truetype("arial.ttf", 68)

    text = "© " + text + "  "
    text_w, text_h = drawing.textsize(text, font)

    pos = w - text_w, (h - text_h) - 50

    c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
    drawing = ImageDraw.Draw(c_text)

    drawing.text((0,0), text, fill="#ffffff", font=font)
    c_text.putalpha(100)

    photo.paste(c_text, pos, c_text)
    photo.save(Output_images)



list = glob.glob('Source_images/in/*.*')
for photo in list:

    out = photo.replace('in','out')
    copyright_apply(photo,out,photo[17:-4])




