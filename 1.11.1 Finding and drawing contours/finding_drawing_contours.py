# python finding_drawing_contours.py -i basic_shapes.png
# python finding_drawing_contours.py -i coins02.png
# python finding_drawing_contours.py -i m.jpg
# python finding_drawing_contours.py -i clonazepam_1mg.png
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
auto = cv2.Canny(blurred, 10, 200)

# find all contours in the image and draw ALL contours on the image
cnts = cv2.findContours(auto.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Instruct to return a list of all contours in the image by passing 
# in the cv2.RETR_LIST. This flag will ensure that all contours are returned. Other methods exist,
# such as returning only the external most contours.

cnts = imutils.grab_contours(cnts)
clone = image.copy()
# cv2.drawContours(Image_name, Contors, index_of_the_contor_-1_for_all_contors, color, thiknes)
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print("Found {} contours".format(len(cnts)))

cv2.imshow("All Contours", clone)
cv2.imshow("All auto", auto)
cv2.waitKey(0)

cv2.destroyAllWindows()
clone = image.copy()
for (i, c) in enumerate(cnts):
    print("Drawing contour #{}".format(i + 1))
    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
    cv2.imshow("Single Contour", clone)
    cv2.waitKey(0)

clone = image.copy()
cv2.destroyAllWindows()
# find contours in the image, but this time keep only the EXTERNAL
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print("Found {} EXTERNAL contours".format(len(cnts)))
# show the output image
cv2.imshow("All EXTERNAL contours", clone)
cv2.waitKey(0)


clone = image.copy()
cv2.destroyAllWindows()
for c in cnts:
    # construct a mask by drawing only the current contour
    mask = np.zeros(gray.shape, dtype="uint8")
    cv2.drawContours(mask, [c], -1, 255, -1)
    # show the images
    cv2.imshow("Image", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Image + Mask", cv2.bitwise_and(image, image, mask=mask))
    cv2.waitKey(0)