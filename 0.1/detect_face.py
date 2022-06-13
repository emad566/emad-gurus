from imageio import imwrite
import cv2
image = cv2.imread("m.jpg")
# resize image
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=7, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
for (x, y, w, h) in rects:
	cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Faces", gray)
cv2.waitKey(0)