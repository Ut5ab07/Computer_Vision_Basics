#Motion Detection

import cv2
cap = cv2.VideoCapture(0)
ret,frame1 = cap.read()
frame1 = cv2.flip(frame1,1)
gray1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
gray1=cv2.GaussianBlur(gray1,(5,5),0) #remove noise from the image

while True:
    ret, frame2 = cap.read()
    frame2 = cv2.flip(frame2,1)
    gray2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    gray2=cv2.GaussianBlur(gray2,(5,5),0)

    diff = cv2.absdiff(gray1,gray2)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=2)
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(frame2,(x,y),(x+w,y+h),(255,120,60),-10)

    cv2.imshow("MOtion detector", frame2)
    gray1 = gray2.copy()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

cap.release()
cv2.destroyAllWindows()