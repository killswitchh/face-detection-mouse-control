import numpy as np
import cv2
import pyautogui

pyautogui.FAILSAFE=False

#https://github.com/trane293/Palm-Fist-Gesture-Recognition
#https://github.com/Aravindlivewire/Opencv/tree/master/haarcascade
#closed_palm = cv2.CascadeClassifier('open_palm.xml')
#open_palm = cv2.CascadeClassifier('closed_palm.xml')


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap=cv2.VideoCapture(0)
oldcx=0
oldcy=0
while 1:
  ret,img = cap.read()
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray,1.3,5)

  sx,sy=pyautogui.size()
  for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    #find center
    cx=x+w//2
    cy=y+h//2
    cv2.rectangle(img,(cx,cy),(cx+2,cy+2),(0,255,0),2)
    
    diffx=(cx-oldcx)*4
    diffy=(cy-oldcy)*4
    pyautogui.moveRel(diffx,diffy)
    oldcx=cx
    oldcy=cy
  
  cv2.imshow('Output',img)
  cv2.resizeWindow('Output',sx//4,sy//4)


  k=cv2.waitKey(30) & 0xff
  if (k==27):
    break
cap.release()
cv2.destroyAllWindows()
