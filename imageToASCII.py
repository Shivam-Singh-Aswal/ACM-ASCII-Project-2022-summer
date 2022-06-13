import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

folder_path = "images"
image_name = 'MS-DHONI.jpg'
path = folder_path+'/'+image_name  #Path of the image file
img = cv2.imread(path, 1)  #open the image

asciiCharList = "$@B%8&WM#oahkbdpqwmZO0QLCJUYXzcvunxrjft*/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


#Get intensity of pixel group
def getGroupIntensity(image, groupSize, point):
    intensity = 0
    if point[0]+groupSize[0] < image.shape[0]:
        endRow = point[0]+groupSize[0]
    else:
        endRow = image.shape[0]
    if point[1]+groupSize[1] < image.shape[1]:
        endCol = point[1]+groupSize[1]
    else:
        endCol = image.shape[1]

    for i in range(point[0], endRow):
        for j in range(point[1], endCol):
            intensity += image[i][j]

    intensity = intensity/((endRow-point[0])*(endCol-point[1]))  #Averaging the intensity
    index = round(intensity*(len(asciiCharList)-1)/255)
    return index


#Setting the background color
bg_color_codes = {
    "black":0,
    "white":255,
    "grey":40
}
bg_color = bg_color_codes["black"]

#Setting font type
font = ImageFont.truetype("DejaVuSansMono.ttf", 20)
char_size = font.getsize("A")

#For GrayScale
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Image resolution and Pixel group sizing and scale
scale = 2
space = scale*char_size[0]-char_size[1]
groupSize = eval(input())
out_size = (image.shape[1]//groupSize[0]*char_size[0]*scale, image.shape[0]//groupSize[1]*(char_size[1]+space))
print(out_size)
print(image.shape)
print(char_size)
asciiImage = Image.new('L', out_size, bg_color)
draw = ImageDraw.Draw(asciiImage)



#For each pixel-Group in image provide an ascii character based on the intensity (GrayScale)
for i in range(image.shape[0]//groupSize[0]):
    row = ''
    for j in range(image.shape[1]//groupSize[1]):
        index = getGroupIntensity(image, groupSize, (i*groupSize[0], j*groupSize[1]))
        if bg_color >= 150:
            character = asciiCharList[index]
        else:
            character = asciiCharList[-(index+1)]
        #draw.text((scale*j*(char_size[0]),(char_size[1]+space)*i), character*scale, fill = 255-bg_color, font = font)
        row = row + character*scale
    #draw.text_kerning = -3
    draw.text((0,(char_size[1]+space)*i), row, fill = 255-bg_color, font = font)


#Creating ascii image for RGB




#Saving the results to a text file
asciiImage.save("AsciiImages/"+image_name)
