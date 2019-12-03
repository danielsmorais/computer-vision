import cv2
import numpy as np
import argparse


cv2.namedWindow('result')


cap = cv2.VideoCapture('video.mp4')
  
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
    lower_blue = np.array([0, 49, 190])
    upper_blue = np.array([65, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask=mask)


    # find contours in the thresholded image
    # find contours in the binary image
    img, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
      # calculate moments for each contour
      M = cv2.moments(c)
    
      # calculate x,y coordinate of center
      cX = int(M["m10"] / M["m00"])
      cY = int(M["m01"] / M["m00"])
      cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
      cv2.putText(img, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
      # display the image
      cv2.imshow("Image", img)


    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)


    #---------------------------------------------------------------
    # Display the resulting frame
    #cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()