# watermarked_pictures
# Add a Copyright or Watermark to Photos Using Python
#I use a handy Python library called Pillow. Install it by using the following command in your terminal:
$ pip install pillow


# import a couple of modules from the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# After that, we use the first module image to open an image. Opening an image makes it possible to perform operations on it.
photo = Image.open(‘yourimage/filename.jpg’)

 
# Store image width and height
w, h = photo.size
print(w,h)


# Next, we make the image drawable and set a font for our copyright text:
# make the image editable
drawing = ImageDraw.Draw(photo)
font = ImageFont.truetype("arial.ttf", 68)


# Next is to set the copyright text and at the same time store the width and height of that text :
# get text width and height
text = "© Robbert Brouwers  "
text_w, text_h = drawing.textsize(text, font)




# calculate where the copyright text will be placed:
pos = w - text_w, (h - text_h) - 50


# create a new image that has the size of the copyright text and give that a background color and opacity, then place the text in this image and place this complete image on top of the original photo:
c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
drawing = ImageDraw.Draw(c_text)
drawing.text((0,0), text, fill="#ffffff", font=font)
c_text.putalpha(100)



# We now have our photo and a copyright image that we want to place on top of the photo on the position we’ve defined as pos:
photo.paste(c_text, pos, c_text)
photo.save('yourimage/filename_out.jpg')



# I have created a folder called Source_images and in that folder I’ve created two more folders: in and out. In the in folder I’ve placed two photos that I would like to apply a watermark to.



# glob is another handy library that allows us to get all filenames in a specific folder
import glob
list = glob.glob("Source_images/in/*.*")
print(list)

