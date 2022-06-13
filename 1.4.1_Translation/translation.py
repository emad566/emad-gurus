# python translation.py -i m.jpg
import cv2
import argparse
import numpy as np

def translate(img, x, y):
    M = np.float32([[1,0,x], [0,1,y]])
    shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return shifted
    
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path of the image" )
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)
translated = translate(image, 50, 100)
cv2.imshow("translated", translated)
cv2.waitKey(0)