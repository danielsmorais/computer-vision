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
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    

    # loop over the contours
    for c in cnts:
      # compute the center of the contour
      M = cv2.moments(c)
      cX = int(M["m10"] / M["m00"])
      cY = int(M["m01"] / M["m00"])
    
      # draw the contour and center of the shape on the image
      cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
      cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
      cv2.putText(image, "center", (cX - 20, cY - 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
      # show the image
      cv2.imshow("Image", image)



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