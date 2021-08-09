
import os
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
os.startfile("ufo.txt")
cap = cv2.VideoCapture(0)

a=0
while 1:
    if a==0:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        
        cv2.imshow('img',img)
        if len(faces) == 0 | a==0:
            a=a+1
            print("protection activated")
            os.system('TASKKILL /F /IM notepad.exe') # mp4 için wmplayer.exe
            cap.release()
            cv2.destroyAllWindows()
    
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

#Erdem Erbaba
