import numpy as np
import cv2
canvas = np.zeros((300, 300, 3), dtype="uint8")


red = (0, 0, 255)
yellow = (0, 255, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.line(canvas, (0, 0), (300, 300), red, 3)
cv2.rectangle(canvas, (0, 0), (150, 150), yellow, 3)

for r in range(0,125, 25):
    cv2.circle(canvas, (225, 225), r, (255,255,255), 3)
    
for i in range(0, 5):
	radius = np.random.randint(5, high=76)
	color = np.random.randint(0, high=256, size = (3,)).tolist()
	pt = np.random.randint(0, high=75, size = (2,))
	cv2.circle(canvas, tuple(pt), radius, color, -1)


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)