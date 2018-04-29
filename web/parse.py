# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

def parse_text(file_name):
	pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

	# construct the argument parse and parse the arguments

	# load the example image and convert it to grayscale

	image = cv2.imread(file_name)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# check to see if we should apply thresholding to preprocess the
	# image

	# write the grayscale image to disk as a temporary file so we can
	# apply OCR to it
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	# load the image as a PIL/Pillow image, apply OCR, and then delete
	# the temporary file
	text = pytesseract.image_to_string(Image.open(filename))
#	os.remove(filename)
	# print(text)
#	textfile = open("text.txt", "w+")
#	textfile.write(text)
#	textfile.close()
	return text

	# show the output images
	# cv2.imshow("Image", image)
	# cv2.imshow("Output", gray)
	# cv2.waitKey(0)
