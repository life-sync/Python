import cv2
import numpy

img = cv2.imread('Mini-Projects/Haar_Cascade_Classifier/Data/FaceBarca.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('Mini-Projects/Haar_Cascade_Classifier/Data/haarcascade_frontalface_default.xml')


faces = face_cascade.detectMultiScale(gray,1.2,5)
# print(faces)

# faces = face_cascade.detectMultiScale(gray,1.7,5) # ScaleFactor

# faces = face_cascade.detectMultiScale(gray,1.5,0) # minNeigbours
# faces = face_cascade.detectMultiScale(gray,1.1,7) # minNeigbours

for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
