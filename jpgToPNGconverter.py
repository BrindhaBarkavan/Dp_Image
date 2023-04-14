import sys
import os
from PIL import Image
from pygments.formatters import img

# grab the first and second arguments from terminal
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if folder exists , if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the image folder convert to png ,save into output folder
for filename in os.listdir(image_folder):
    image = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    image.save(f'{output_folder}{clean_name}.png', 'png')
    print('All Done! ')
