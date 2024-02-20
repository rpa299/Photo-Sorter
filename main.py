from exif import Image
import os

images = os.listdir('photos')
for image in images:
    with open(f'photos/{image}','rb') as image_file:
        image = Image(image_file)
        print(image.datetime)
