# python tictactoe.py -i tictactoe.png
import cv2
import imutils
import argparse 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for (i, c) in enumerate(cnts):
    area = cv2.contourArea(c)
    (x, y, w, h) = cv2.boundingRect(c)

    hull = cv2.convexHull(c)
    hullArea = cv2.contourArea(hull)
    solidity = area / float(hullArea)
    
    char = "?"
    
    if solidity > 0.9:
        char = "O"
        
    elif solidity > 0.5:
        char = "X"

    print(char)
    if char != "?":
        char +=str(i)
        cv2.drawContours(image, [c], -1, (0, 255, 0), 3)
        cv2.putText(image, char, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.25,
            (0, 255, 0), 4)
            


    print("{} (Contour #{}) -- solidity={:.2f}".format(char, i + 1, solidity))
    
cv2.imshow("Output", image)
cv2.waitKey(0)