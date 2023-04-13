# import required library
from PIL import Image

# open the image you want to convert
im = Image.open("dp1.jpg")

# check the size using "print(im.size)" if needed

# check the format using "print(im.format)"

# change the image into thumbnail
im.thumbnail((150, 150))

# save the image
im.save("wattsapp_dp1.jpg")

# preview the image
im.show()
