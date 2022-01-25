import os
import numpy as np
from PIL import Image

try:
    directory = '/app/raw-images/1024px'

    image_count = 0

    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            print("\nChecking Shape of JPG ({})... ".format(filename))

            img = Image.open(directory + '/' + filename)
            array = np.array(img)
            print("{}\n".format(array.shape)) 

            image_count = image_count + 1

            continue
        else:
            continue

except Exception as e:
    print("Exception Caught\n\n{}".format(e))

print("Images found: {}...\n".format(image_count))