# python rotation.py -i m.jpg
import cv2
import argparse
import numpy as np

def rotate(image, angle, center=None, scale=1.0):
	(h, w) = image.shape[:2]
	
	if center is None:
		center = (w / 2, h / 2)
  
	M = cv2.getRotationMatrix2D(center, angle, scale)
	rotated = cv2.warpAffine(image, M, (w, h))
	return rotated

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path of the image" )
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

rotated = rotate(image, 50)
cv2.imshow("rotated", rotated)
cv2.waitKey(0)