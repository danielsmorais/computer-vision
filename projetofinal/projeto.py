import cv2
import numpy as np
#import matplotlib.pyplot as plt
import argparse


cap = cv2.VideoCapture('video.mp4')

#f= open("dados.txt","w+")
  
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    #---------------------------------------------------------------
    # calculos 
    #HSV - segmentacao
    #conversao
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #definicao do range
    #lower_blue = np.array([0, 49, 190])
    lower_blue = np.array([0, 93, 126])
    upper_blue = np.array([65, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask=mask)

    # find contours in the thresholded image
    # find contours in the binary image

    img, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    c = max(contours, key = cv2.contourArea)
    M = cv2.moments(c)
    
    # calculate x,y coordinate of center
    if M["m00"] != 0:
      cX = int(M["m10"] / M["m00"])
      cY = int(M["m01"] / M["m00"])
    else:
      cX, cY = 0, 0

    text = "("+str(cX)+","+str(cY)+")"
    cv2.putText(frame, text, (30, 450),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.circle(frame, (cX, cY), 4, (255, 0, 0), -1)
  
    # display the image
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    #f.write(str(cX)+" "+str(cY)+"\n")

    #---------------------------------------------------------------
    # Display the resulting frame
    #cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
#f.close() 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()