import cv2
import numpy as np


"""Functions Definitions"""
#The function to convert the color image to a grayscale image
def toGrayScale(image, algo= "average"):
    fn = funcPick[algo]
    transform = []

    for i in range(image.shape[0]):
        rowEntry = []
        for j in range(image.shape[1]):
            luminosity = fn(image[i][j])
            rowEntry.append(element)
        transform.append(rowEntry)

    transform = np.array(transform)/255
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


"""Name of algorithm vs function"""
funcPick = {
    "average": averageFn,
    "max-min": minMaxFn,
    "weightedAvg" : weightedAvgFn
}

"""Main Body"""
path = "minion.jpg"

originalImage = cv2.imread(path, 1)
orgGrayScale = cv2.imread(path, 0)
cv2.imshow("Original Image", originalImage)
cv2.imshow("Original Gray Image", orgGrayScale)

#Conversion to various types of grayscales
grayimage_averaged = toGrayScale(originalImage)
grayimage_minMaxFn = toGrayScale(originalImage, "max-min")
grayimage_weightedAvg = toGrayScale(originalImage, "weightedAvg")

cv2.imshow("Averaged GrayScale Image", grayimage_averaged)
cv2.imshow("minMaxed GrayScale Image", grayimage_minMaxFn)
cv2.imshow("WeightedAvg GrayScale Image", grayimage_weightedAvg)
cv2.waitKey(0)
cv2.destroyAllWindows()
