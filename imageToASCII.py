import numpy as np 
import cv2
from PIL import Image, ImageDraw, ImageOps, ImageFont
import pdb 

#Setting the folder path for opening image
FOLDER_PATH = "images"


#The list of ascii character in increasing order of intensity
ASCII_CHARLIST = "$@B%8&WM#oahkbdpqwmZO0QLCJUYXzcvunxrjft*/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
#ASCII_CHARLIST = "@B&ma+*:. "
#ASCII_CHARLIST = "@@@@@@@@"

#Setting font type and setting up scale to make square pixel
FONT = ImageFont.truetype("DejaVuSansMono.ttf", 20)
char_size = FONT.getsize("A")
scale = 2
space = scale*char_size[0]-char_size[1]


"""The GrayScale ASCII Image"""

#Setting the background color
def give_bg_color(color):
    bg_color_codes = {
        "black":0,
        "white":255,
        "grey":40
    }
    return bg_color_codes[color]

#Get intensity of pixel group around the given point for both RGB and GrayScale images 
def getGroupIntensity(image, groupSize, point):
    """
    Returns the average intensity of the grouped pixels
    """
    intensity = image[point[0]][point[1]]*0 #initialise the return value to zero scalar or vector 

    #Define a group using group size values (limited by image size)
    endRow = min(point[0]+groupSize[0], image.shape[0])
    endCol = min(point[1]+groupSize[1], image.shape[1])

    size = (endRow-point[0])*(endCol-point[1])  #No of elements in the group 

    #sum all the intensities with averaging in the group
    for i in range(point[0], endRow):
        for j in range(point[1], endCol):
            intensity = intensity + image[i][j]/size 

    return intensity

def createGrayASCII(img, groupSize):
    """
    Returns the ascii character image
    """
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #Converting the color image to grayscale

    #The background color
    bg_color = give_bg_color("black")

    #The output image resolution
    out_size = (image.shape[1]//groupSize[0]*char_size[0]*scale, image.shape[0]//groupSize[1]*(char_size[1]+space))
    asciiImage = Image.new('L', out_size, bg_color)  #Create a image handle of required size
    draw = ImageDraw.Draw(asciiImage)

    #For each pixel-Group in image provide an ascii character based on the intensity (GrayScale)
    for i in range(image.shape[0]//groupSize[0]):
        row = ''
        for j in range(image.shape[1]//groupSize[1]):
            intensity = getGroupIntensity(image, groupSize, (i*groupSize[0], j*groupSize[1]))
            #pick out apt. index corresponding to avg intensity
            index = round(intensity*(len(ASCII_CHARLIST)-1)/255)
            if bg_color >= 150:
                character = ASCII_CHARLIST[index]
            else:
                character = ASCII_CHARLIST[-(index+1)]
            #draw.text((scale*j*(char_size[0]),(char_size[1]+space)*i), character*scale, fill = 255-bg_color, font = FONT)
            row = row + character*scale
        draw.text((0,(char_size[1]+space)*i), row, fill = 255-bg_color, font = FONT)

    return asciiImage


"""The RGB ASCII Image"""

def main(image_name):
    #Opening the image file
    path = FOLDER_PATH + '/' + image_name  #Path of the image file
    img = cv2.imread(path, 1)  #open the image
    print(img.shape)

    #Image resolution and Pixel group sizing and scale
    groupSize = eval(input())

    #Creating black and white ascii image of the input image 
    #asciiImage = createGrayASCII(img, groupSize)

    #Creating coloured ascii image of the input image 
    asciiImage = createRGB_ASCII(img, groupSize)

    #Saving the results to a text file
    asciiImage.save("AsciiImages/"+image_name)


#Creating ascii image for RGB
def createRGB_ASCII(image, groupSize):
    """
    Returns the ascii character colored image
    """
    #The background color
    white = np.array([255, 255, 255])
    bg_color = np.array([0,0,0])

    #The output image resolution
    out_size = (image.shape[1]//groupSize[0]*char_size[0]*scale, image.shape[0]//groupSize[1]*(char_size[1]+space))
    asciiImage = Image.new('RGB', out_size, tuple(bg_color))  #Create a image handle of required size
    draw = ImageDraw.Draw(asciiImage)

    #For each pixel-Group in image provide an ascii character based on the intensity (GrayScale)
    for i in range(image.shape[0]//groupSize[0]):
        for j in range(image.shape[1]//groupSize[1]):
            #intensity is in 'BGR' and we require 'RGB' so invert it
            intensity = getGroupIntensity(image, groupSize, (i*groupSize[0], j*groupSize[1])).astype(int)
            color = tuple(list(intensity)[::-1])
            index = round(0.33*sum(intensity)*(len(ASCII_CHARLIST)-1)/255)
            character = ASCII_CHARLIST[index]
            
            draw.text((scale*j*(char_size[0]),(char_size[1]+space)*i), character*scale, fill = color, font = FONT)
    return asciiImage


print("Name of file: ", end = "")
main(input())

