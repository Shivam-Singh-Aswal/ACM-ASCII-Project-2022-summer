# ACM-ASCII-Project-2022-summer 

## Description
This project was completed in the summer vacation 2022. It is based on the conversion of a regular pixel image to ASCII art, both to grayscale and colored.
Further it has also the programs to convert a video file to ascii art video. This project includes following python files
- convertToGrayScale.py (This file converts given input RGB image file to grayscale image file)
- imageToASCII.py (This file can be used to convert any image file to ascii art image,either RGB or Grayscale)
- asciiVideo.py (This file makes use of imageToASCII.py code to convert a regular video file to ascii art video)

## Language Used 
Python

## Libraries used
- cv2
- Numpy
- PIL 

## How to run the project
To run the files follow these steps..

a) For convertToGrayScale.py 
- Just run the file and provide the input RGB image file path at the runtime. 
- Various outputs from various conversion functions will be shown on the screen.

b) For imageToASCII.py 
- Put the input image file in the image folder and input the name of image at the runtime. 
- Specify the conversion type (RGB or Grayscale)
- Also input the required output size (in terms of characters, as 100x100 means 100 character lines with 100 chars in each line).
- The output file will be saved in the image folder as "ascii_<input_file_name>.jpg>

c) For asciiVideo.py 
- Put the input video file in the video folder and input the name of video at the runtime. 
- Specify the conversion type (RGB or Grayscale).
- The output file will be saved in the video folder as "ascii_<input_file_name>.mp4>

In case of any difficulty go through the comments of code files. I have also included sample input and output files in the images and video folders.


## My learning takeaways
I enjoyed doing this project as I learnt to use some of interesting image and video manipulation tools in python. 

## References
- https://hackmd.io/@xenorivai/H12U8cwv5
- https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjMpPP5s7b4AhUE-zgGHfQfDm0QFnoECAQQAQ&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FASCII&usg=AOvVaw2HzUa6hy2uH7luG7ejFlib
- https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjPvtiHtLb4AhXG7jgGHR4sBUkQFnoECAQQAQ&url=https%3A%2F%2Fpypi.org%2Fproject%2Fopencv-python%2F&usg=AOvVaw3ZlQ0giNOPompJrAzIptzx
