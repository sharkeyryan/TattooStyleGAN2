import os
import numpy as np
from PIL import Image

try:
    directory = '/app/raw-images/1024px'

    image_count = 0
    image_shares = 0


    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            print("Checking Shape of JPG ({})...\n".format(filename))

            img = Image.open(directory + '/' + filename)
            array = np.array(img)
            print("Shape is... {}\n".format(array.shape)) 

            image_count = image_count + 1

            continue
        else:
            continue

except Exception as e:
    print("Exception Caught\n\n{}".format(e))

print("Images found: {}...\n".format(image_count))
print("Images resized: {}...\n".format(image_resized))