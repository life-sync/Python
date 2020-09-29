import cv2
import numpy

img = cv2.imread('Mini-Projects/Haar_Cascade_Classifier/Data/car.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('Mini-Projects/Haar_Cascade_Classifier/Data/haarcascade_russian_plate_number.xml')

faces = face_cascade.detectMultiScale(gray,1.85,5)
# print(faces)

for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)
cv2.imwrite("LicensePlate_Detected.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
