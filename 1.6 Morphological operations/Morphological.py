# python Morphological.py  -i m.jpg
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# #Erosion
for i in range(1, 15):
	eroded = cv2.erode(gray.copy(), None, iterations=i)
	cv2.imshow("Eroded {} times".format(i), eroded)
	cv2.waitKey(0)

# #Dilation
for i in range(1, 15):
	eroded = cv2.dilate(gray.copy(), None, iterations=i)
	cv2.imshow("dilated {} times".format(i), eroded)
	cv2.waitKey(0)

#Opening
# cv2.destroyAllWindows()

# cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7), (9, 9), (11, 11), (13, 13)]
for kernelSize in kernelSizes:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	print(kernel)
	opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
	cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opening)
	cv2.waitKey(0)
 
 # closeing
cv2.destroyAllWindows()
cv2.imshow("Original", image)
for kernelSize in kernelSizes:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
	cv2.imshow("Closing: ({}, {})".format(kernelSize[0], kernelSize[1]), closing)
	cv2.waitKey(0)
 
 # MORPH_GRADIENT
cv2.destroyAllWindows()
cv2.imshow("Original", image)
for kernelSize in kernelSizes:
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
	cv2.imshow("Gradient: ({}, {})".format(kernelSize[0], kernelSize[1]), gradient)
	cv2.waitKey(0)