import cv2
import numpy as np

def nothing(x):
    pass


cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h1,s1,v1 = 100,100,100
h2,s2,v2 = 100,100,100

# Creating track bar
cv2.createTrackbar('h1', 'result',0,179,nothing)
cv2.createTrackbar('s1', 'result',0,255,nothing)
cv2.createTrackbar('v1', 'result',0,255,nothing)
cv2.createTrackbar('h2', 'result',0,179,nothing)
cv2.createTrackbar('s2', 'result',0,255,nothing)
cv2.createTrackbar('v2', 'result',0,255,nothing)

 
# cap = cv2.VideoCapture('video.mp4')
# ret, frame = cap.read()

frame = cv2.imread('foto.jpg')

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
ret = True

  
# Read until video is completed
while(True):
  if ret == True:
    #---------------------------------------------------------------
    # calculos 
    #HSV - segmentacao
    #conversao
    

    # get info from track bar and appy to result
    h1 = cv2.getTrackbarPos('h1','result')
    s1 = cv2.getTrackbarPos('s1','result')
    v1 = cv2.getTrackbarPos('v1','result')
    h2 = cv2.getTrackbarPos('h2','result')
    s2 = cv2.getTrackbarPos('s2','result')
    v2 = cv2.getTrackbarPos('v2','result')    

    #definicao do range
    lower_blue = np.array([h1, s1, v1])
    upper_blue = np.array([h2, s2, v2])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask=mask)

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