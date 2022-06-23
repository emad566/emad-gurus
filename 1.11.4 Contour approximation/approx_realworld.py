# python approx_realworld.py -i receipt.png
import cv2
import imutils
import argparse 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 75, 200)

cv2.imshow("Original", image)
cv2.imshow("Edge Map", edged)
cv2.waitKey(0)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:7]
for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.01 * peri, True)
	print("original: {}, approx: {}".format(len(c), len(approx)))
    
	if len(approx) == 4:
		cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
        
cv2.imshow("Output", image)
cv2.waitKey(0)