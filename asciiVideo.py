"""
This program converts any video media to ASCII art video 
"""

import cv2
from numpy import asarray
from imageToASCII import createRGB_ASCII, createGray_ASCII


#Function to convert the video file into a list of frames 
def getFramesFromVideo(video_path, reqFrameRate):
	"""
	Inputs:
		video_file_path 	: string 
		frame_rate_required : int/float
	Return:
		frameBook : list of all the frames from original video
	"""
	#Opening the file 
	video = cv2.VideoCapture(video_path)
	#Extracting the frame rate value of the original video
	frameRate = video.get(cv2.CAP_PROP_FPS)

	frameBook = []

	#Defining the step value, to jump frames (+1 since step can't be zero)
	step = int(frameRate/reqFrameRate) + 1 

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
	Inputs:
		frameBook : list - the list of all the ascii frames 
		frameRate : int/float - desired fps for the output video
		frameSize : tuple - the dimensions of the output video frames'
		outPath   : string - the destination folder
	Return:
		Boolean value : true if succesfull, otherwise false  
	"""
	#define the codec for resulting video 
	codec = cv2.VideoWriter_fourcc(*'MJPG')
	writer = cv2.VideoWriter(outPath, codec, float(frameRate), frameSize, 1)  #Creating the video handle 
	#Add the frames to the video 
	for frame in frameBook:
		writer.write(frame)
	writer.release()
	return "Done" 

#main 
def main():
	#Parameters for ascii Video
	outPath = "AsciiVideos/newtons_balls.avi"
	frameRate = 5	   	
	frameSize = None 	
	asciiFrameBook = []   #This is the list of all the frames converted to ascii art image

	#Generate the Ascii frame book
	frameBook = getFramesFromVideo("videos/newtons_balls.mp4", frameRate)
	print("Video converted to pixel frames! \nSize = ", len(frameBook))   #Print the status 
	
	groupSize = (5,5)
	 
	#Convert each frame to ascii Image 
	counter = 0 
	for img in frameBook:
		counter += 1
		asciiFrameBook.append(asarray(imageToASCII.createRGB_ASCII(img, groupSize)))
		print("Frame {0} converted".format(counter))

	
	#Stitch all the frames together to form a video and print the status 
	#The frame dimensions are inverted to have the form (width, height), instead of (height, width) 
	#as required by the cv2.VideoWriter function 
	frameSize = asciiFrameBook[0].shape[1::-1]   
	print("Frame-Size is : ", frameSize)
	print(getVideoFromFrames(asciiFrameBook, frameRate, frameSize, outPath))


#Call the main function 
if __name__ == "main":
	main()