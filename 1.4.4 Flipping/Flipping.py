# python Flipping.py -i m.jpg
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path of the image" )
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

# -1-> flip the image along both axes
# 0-> flip the image vertically
# 1-> flip the image horizontally
cv2.imshow("flipped", cv2.flip(image, -1))
cv2.waitKey(0)