"""
@author: VARUN
"""

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    b, l, d = img.shape
    capCenter = ((l)//2, (b)//2)
    for (x,y,w,h) in faces:
        faceCenter = (((x)+(x+w))//2,((y)+(y+h))//2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.circle(img, faceCenter, 3, (0, 255, 0), -1)
        cv2.circle(img, capCenter, 3, (0, 255, 255), -1)
        cv2.line(img, faceCenter, capCenter, (255, 255, 255), 1)
        xyCoo = [capCenter[0] - faceCenter[0], capCenter[1] - faceCenter[1]]
        faceArea = 33124
        if (w*h) == faceArea:
            zCoo = [0]
            z= ", Awesome"
        elif (w*h) < faceArea:
            zCoo = [1]
            z= ", Go Front"
        elif (w*h) > faceArea:
            zCoo = [-1]
            z= ", Go Back"
        coo = xyCoo + zCoo
        cv2.putText(img, str(coo), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        if (faceCenter == capCenter) or
            (faceCenter[0] in range(capCenter[0]-15, capCenter[0]+15)) and
            (faceCenter[1] in range(capCenter[1]-15, capCenter[1]+15)):
            text = "Perfect"
        else:
            if faceCenter[1] < capCenter[1]:
                text = "Down"
            elif faceCenter[1] > capCenter[1]:
                text = "Up"
            elif faceCenter[0] < capCenter[0]:
                text = "Right"
            elif faceCenter[0] > capCenter[0]:
                text = "Left"
        cv2.putText(img, text+z, (faceCenter[0]+100, faceCenter[1]+100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff == 'q'
        if k == 27:
            break
cap.release()
cv2.destroyAllWindows()
