import os
from core.scanner import DocScanner

scanner = DocScanner(interactive=True)

image = input('Enter the path to the image')    #Comment out this line or the next one
#image = '' #Add the path to image               #Any one of these two is required

if os.path.isdir(image):
    for img in [i for i in os.listdir(image) if i.lower.endswith(('.jpg', '.jpeg', '.png'))]:
        scanner.scan(img)
elif os.path.isfile(image):
    scanner.scan(image)
else:
    print('An error occured, Make sure you are using the correct name')
