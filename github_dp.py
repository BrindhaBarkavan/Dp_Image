# import required library
from PIL import Image , ImageFilter

# open the image you want to convert
im = Image.open("dp1.jpg")

# check the size using "print(im.size)" if needed

# check the format using "print(im.format)"
im.filter(ImageFilter.SHARPEN)
# change the image into thumbnail
im.thumbnail((500, 500))

# save the image
im.save("github_dp1.jpg")

# preview the image
im.show()
