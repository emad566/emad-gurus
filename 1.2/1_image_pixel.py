
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path of the image" )
args = vars(ap.parse_args())
print(args)

image = cv2.imread(args["image"])
(h, w) = image.shape[0:2]
print("image size:({h}, {w})".format(h=h, w=w))
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("(R:{r}, G:{g}:, B:{b})".format(r=r, g=g, b=b))

(cY, cX) = (h//2, w//2)
cv2.imshow("TOP Left", image[0:cY, 0:cX])

image[cY:h, cX:w] = (0, 0, 255)
image[0:cY, cX:w] = (0, 255, 255)

cv2.imshow("Bottom right Red", image)
cv2.waitKey(0)
