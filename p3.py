import cv2
import webbrowser

#Creating a qr code detector object

cap = cv2.VideoCapture(0) #using default system webcam (0)
detector = cv2.QRCodeDetector() #importing the QR code module

a=None #Initialiizing the variable 

while True:
    ret,img = cap.read() 
    if not ret:
        break
    data, bbox, _ =  detector.detectAndDecode(img) #detecting and decoding the QR code

    if data:
        a=data
        print("QR code detected:", a)
        break

    cv2.imshow("QR code detector", img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#open browser only if qr code data found

if a:
    webbrowser.open(a)
