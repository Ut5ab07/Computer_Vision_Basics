import cv2
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img=cv2.imread('assets/faces.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,3) #(scaling factor, min neighbors)
for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(140,255,240),2)

cv2.imshow('Detected Face',img )
if cv2.waitKey(0):
    cv2.destroyAllWindows()
