# python Cropping.py -i m.jpg
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path of the image" )
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

cv2.imshow("croped", image[0:200, 150:350 ])
cv2.waitKey(0)