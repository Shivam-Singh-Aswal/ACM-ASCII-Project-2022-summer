"""
This programs converts an RGB image to grayscale by using various conversion methods 
We just have to convert the RGB tuple to a scalar value representing luminosity of the pixel
which can be achieved by various mathematical fn e.g., average, max etc.
"""
import cv2
import numpy as np


"""
Functions Definitions
"""

#The function to convert the color image to a grayscale image
def toGrayScale(image, algo= "average"):
    fn = funcPick[algo] #Pick one conversion method 
    transform = []      #The grayscale image array 

    for i in range(image.shape[0]):
        rowEntry = []
        for j in range(image.shape[1]):
            luminosity = fn(image[i][j])    #Converting RGB tuple to grayscale scalar
            rowEntry.append(element)
        transform.append(rowEntry)

    transform = np.array(transform)/255     #The grayscale values range from 0 to 1, unlike 0 to 255 for RGB values
    return transform

#The averaging function
def averageFn(rgbTuple):
    return sum(rgbTuple)/3


#The min value max value fn
def minMaxFn(rgbTuple):
    return 0.5*max(rgbTuple)+0.5*min(rgbTuple)


#The weighted average function 
def weightedAvgFn(rgbTuple):
    r, g, b = rgbTuple
    return 0.21*r+0.72*g+0.07*b


#Name of conversion method vs function for the same
funcPick = {
    "average": averageFn,
    "max-min": minMaxFn,
    "weightedAvg" : weightedAvgFn
}


#main
def main()
    path = "minion.jpg"

    #THe original image 
    originalImage = cv2.imread(path, 1)
    cv2.imshow("Original Image", originalImage)

    #Conversion to various types of grayscales
    grayimage_averaged = toGrayScale(originalImage)
    grayimage_minMaxFn = toGrayScale(originalImage, "max-min")
    grayimage_weightedAvg = toGrayScale(originalImage, "weightedAvg")

    #Displaying the converted gray images 
    cv2.imshow("Averaged GrayScale Image", grayimage_averaged)
    cv2.imshow("minMaxed GrayScale Image", grayimage_minMaxFn)
    cv2.imshow("WeightedAvg GrayScale Image", grayimage_weightedAvg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
