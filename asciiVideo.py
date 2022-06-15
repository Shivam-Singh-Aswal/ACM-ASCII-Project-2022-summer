import cv2
from numpy import asarray
from PIL import Image
import imageToASCII 


#Function to convert the video file into a list of frames 
def getFramesFromVideo(video_path, reqFrameRate):
	"""
	This function takes video file name and required frame rate as input and outputs frame list
	"""
	video = cv2.VideoCapture(video_path)
	frameRate = video.get(cv2.CAP_PROP_FPS)
	frameBook = []

	#Defining the step value to jump frames (+1 since it shouldn't return zero)
	step = int(frameRate/reqFrameRate) + 1 
	#print(step)

	while True:
		working, frame = video.read()  	#Get the current frame 
		if working:   					#Check if video is still left to unframe
			frameBook.append(frame)     #Add the frame to the list 
			for i in range(step-1):
				video.read()   			#Omit the extra frames 
		else:
			break

	return frameBook


#Function to convert the frames of array to a video of desired frame rate
def getVideoFromFrames(frameBook, frameRate, frameSize, outPath):
	"""
	Takes array of ascii frames, frame rate of ascii video and the file location where video is to be saved 
	(with the name of output video)	as input and outputs boolean value representing action completed.
	"""
	fourcc = cv2.VideoWriter_fourcc(*'MJPG')
	writer = cv2.VideoWriter(outPath, fourcc, float(frameRate), frameSize, 1)  #Creating the video handle 
	#Add the frames to the video 
	for frame in frameBook:
		writer.write(frame)
	writer.release()
	return "Done" 

#main 
def main():
	#Parameters for ascii Video
	frameRate = 5
	outPath = "AsciiVideos/newtons_balls.avi"

	#Generate the Ascii frame book
	frameBook = getFramesFromVideo("videos/newtons_balls.mp4", frameRate)
	print("Video converted to pixel frames! Size= ", len(frameBook))
	groupSize = (5,5)
	asciiFrameBook = []

	counter = 0 
	for img in frameBook:
		counter += 1
		asciiFrameBook.append(asarray(imageToASCII.createRGB_ASCII(img, groupSize)))
		print("Frame {0} converted".format(counter))

	print(asciiFrameBook[0].shape)
	frameSize = asciiFrameBook[0].shape[1::-1]
	print(frameSize)
	#Print the status 
	print(getVideoFromFrames(asciiFrameBook, frameRate, frameSize, outPath))


#Call the main function 
main()