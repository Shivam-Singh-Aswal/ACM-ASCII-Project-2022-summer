"""
This program converts any image media to ASCII art image (RGB and GrayScale) 
"""

import numpy as np 
import cv2
from PIL import Image, ImageDraw, ImageOps, ImageFont

#Setting the folder path for opening image
FOLDER_PATH = "images"


#The list of ascii character in increasing order of intensity
#Higher index represents that it will used to replace high intensity pixel
ASCII_CHARLIST = "$@B%8&WM#oahkbdpqwmZO0QLCJUYXzcvunxrjft*/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
#ASCII_CHARLIST = "@B&ma+*:. "

#Setting font type and setting up scale to make square pixel
FONT = ImageFont.truetype("fonts/DejaVuSansMono.ttf", 20)
char_size = FONT.getsize("A")
scale = 2
space = scale*char_size[0]-char_size[1]


"""
The GrayScale ASCII Image
"""

#Getting the background color code 
def giveGray_bg_color(color):
    bg_color_codes = {
        "black":0,
        "white":255,
        "grey":40
    }
    return bg_color_codes[color]

#Get intensity of pixel group around the given point for both RGB and GrayScale images 
def getGroupIntensity(image, groupSize, point):
    """
    Input: 
        image       : nd array - pixel value array of the image 
        groupSize   : tuple - the no of rows and columns in the group 
        point       : tuple - coordinates of the point 
    Return:
        intensity   : int/array - the average intensity of the group 
    """
    #initialise the return value to zero scalar or vector
    intensity = image[point[0]][point[1]]*0  

    #Define a group using group size values (limited by image size)
    endRow = min(point[0]+groupSize[0], image.shape[0])
    endCol = min(point[1]+groupSize[1], image.shape[1])

    size = (endRow-point[0])*(endCol-point[1])  #No of elements in the group 

    #sum all the intensities with averaging in the group
    for i in range(point[0], endRow):
        for j in range(point[1], endCol):
            intensity = intensity + image[i][j]/size 

    return intensity

#Returns the ascii character image in grayscale
def createGray_ASCII(img, groupSize):
    """
    Input:
        img         : nd array - pixel value array of the image 
        groupSize   : tuple - the no of rows and columns in the group
    Return:
        asciiImage  : Image object - the ascii art of the original image  
    """
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #Converting the color image to grayscale

    #The background color
    bg_color = giveGray_bg_color("black")

    #The output image resolution
    #The output image resolution (char_size and groupSize have entries as (xValue, yValue))
    #image.shape returns (height, width), whereas Image.new takes input as (width, height)
    out_size = (image.shape[1]//groupSize[0]*char_size[0]*scale, image.shape[0]//groupSize[1]*(char_size[1]+space))
    asciiImage = Image.new('L', out_size, bg_color) #Create a image handle of required size
    draw = ImageDraw.Draw(asciiImage)               #draw handle to draw characters on the image

    #For each pixel-Group in image provide an ascii character based on the intensity (GrayScale)
    for i in range(image.shape[0]//groupSize[0]):
        row = ''
        for j in range(image.shape[1]//groupSize[1]):
            intensity = getGroupIntensity(image, groupSize, (i*groupSize[0], j*groupSize[1]))
            #pick out apt. index corresponding to avg intensity
            index = round(intensity*(len(ASCII_CHARLIST)-1)/255)
            if bg_color >= 150:
                character = ASCII_CHARLIST[index] #if bg is whitish then more area char occupies lower index, as usual
            else:
                character = ASCII_CHARLIST[-(index+1)]  #if bg is blackish then more area char is higher in index
            row = row + character*scale
        draw.text((0,(char_size[1]+space)*i), row, fill = 255-bg_color, font = FONT) #Write the row on image

    return asciiImage


"""
The RGB ASCII Image
"""

def giveRGB_bg_color(color):
    bg_color_codes = {
        "black":(0, 0, 0),
        "white":(255, 255, 255),
        "grey":(40, 40, 40)
    }
    return np.array(bg_color_codes[color])

#Returns the ascii character image in grayscale
def createRGB_ASCII(image, groupSize):
    """
    Input:
        img         : nd array - pixel value array of the image 
        groupSize   : tuple - the no of rows and columns in the group
    Return:
        asciiImage  : Image object - the ascii art of the original image  
    """
    #The background color
    white = np.array([255, 255, 255])
    bg_color = giveRGB_bg_color("black")

    #The output image resolution (char_size and groupSize have entries as (xValue, yValue))
    #image.shape returns (height, width), whereas Image.new takes input as (width, height)
    out_size = (image.shape[1]//groupSize[0]*char_size[0]*scale, image.shape[0]//groupSize[1]*(char_size[1]+space))
    asciiImage = Image.new('RGB', out_size, tuple(bg_color))  #Create a image handle of required size
    draw = ImageDraw.Draw(asciiImage)

    #For each pixel-Group in image provide an ascii character based on the intensity (GrayScale)
    for i in range(image.shape[0]//groupSize[0]):
        for j in range(image.shape[1]//groupSize[1]):
            #intensity is in 'BGR' and we require 'RGB' so invert it
            intensity = getGroupIntensity(image, groupSize, (i*groupSize[0], j*groupSize[1])).astype(int)
            color = tuple(list(intensity)[::-1])  #inversion
            index = round(max(intensity)*(len(ASCII_CHARLIST)-1)/255)
            character = ASCII_CHARLIST[index]
            
            draw.text((scale*j*(char_size[0]),(char_size[1]+space)*i), character*scale, fill = color, font = FONT)
    return asciiImage


def main():
    #Opening the image file
    image_name = input("Name of file: ")
    convertTo = input("RGB or Gray?: ")
    path = FOLDER_PATH + '/' + image_name  #Path of the image file
    img = cv2.imread(path, 1)  #open the image

    #Pixel group sizing based on required output resolution
    print("Input Image size: ", img.shape[:2])
    requiredOutSize = eval(input("Required Output size (height, width): "))
    groupSize = (img.shape[1]//requiredOutSize[1], img.shape[0]//requiredOutSize[0])

    #Dictionary mapping word to apt function
    getFunc = {
        "gray": createGray_ASCII,
        "rgb": createRGB_ASCII
    }

    #Call the required function 
    asciiImage = getFunc[convertTo.lower()](img, groupSize)

    #Saving the results to a image file
    asciiImage.save("AsciiImages/"+image_name)


#Call the main function 
if __name__ == "main":
    main()

