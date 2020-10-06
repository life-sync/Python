import cv2

face_cascade = cv2.CascadeClassifier('Data/haarcascade_frontalface_default.xml')
#CascadeClassifier object and file contains the face features

cap=cv2.VideoCapture(0) # Video Capture object

while True:

    ret,img=cap.read() # Reading each frame
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray,1.3,6) # Arguments are (Src image,Scale Factor,Min-neighbours)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
        
    var = cv2.waitKey(1) & 0xFF    # Press ESC key to exit the program
    if var == 27:
        break

    cv2.imshow('face',img)

cap.release()
cv2.destroyAllWindows()