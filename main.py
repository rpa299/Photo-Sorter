from exif import Image
import os

images = os.listdir('Photos')

#loop all IMGs in the Photos folder
for image in images:
    imageName = image
    try:
        #open IMG
        with open(f'Photos/{image}','rb') as image_file:
            image = Image(image_file)
        
        #get IMG date
        imageDate = image.datetime
        imageDateSplit = imageDate.split(':',2)

        #set path to 'Photos/YYYY/MM'
        destination = f'Photos/{imageDateSplit[0]}/{imageDateSplit[1]}'
    
    except:
        #set path to undefined folder because it does not have metadata
        destination = f'Photos/Undefined/'
    
    finally:
        #move IMG to path (create folder if not already there)
        if not os.path.exists(destination):
            os.makedirs(destination)
        os.rename(f'Photos/{imageName}', f'{destination}/{imageName}')