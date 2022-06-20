# python resizing.py -i m.jpg
import cv2
import argparse
import numpy as np

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
	dim = None
	(h, w) = image.shape[:2]
	if width is None and height is None:
		return image
	
	if width is None:
		r = height / float(h)
		dim = (int(w * r), height)
	else:
		r = width / float(w)
		dim = (width, int(h * r))
	
	resized = cv2.resize(image, dim, interpolation=inter)
	return resized

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path of the image" )
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

resized = resize(image, 50)
cv2.imshow("resized", resized)
cv2.waitKey(0)