import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('Mini-Projects/Haar_Cascade_Classifier/Data/haarcascade_frontalface_default.xml')
#CascadeClassifier object and file contains the face features

cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray,1.1,6) 
    # print(faces)

    # faces=face_cascade.detectMultiScale(gray,1.9,6)

    # faces=face_cascade.detectMultiScale(gray,1.1,0) 
    # faces=face_cascade.detectMultiScale(gray,1.6,2) 
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) # Getting the coordinates for the face rectangle
        
    var = cv2.waitKey(1) & 0xFF    
    if var == 27:
        break

    cv2.imshow('face',img)

cap.release()
cv2.destroyAllWindows()
