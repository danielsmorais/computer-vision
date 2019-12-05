import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('result')

h1,s1,v1 = 100,100,100
h2,s2,v2 = 100,100,100

# Criacao do track bar
cv2.createTrackbar('h1', 'result',0,179,nothing)
cv2.createTrackbar('s1', 'result',0,255,nothing)
cv2.createTrackbar('v1', 'result',0,255,nothing)
cv2.createTrackbar('h2', 'result',0,179,nothing)
cv2.createTrackbar('s2', 'result',0,255,nothing)
cv2.createTrackbar('v2', 'result',0,255,nothing)

# Load da imagem para calibracao
frame = cv2.imread('foto.jpg')

# conversao de espaco de cor
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

while(True):

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
  lower_color = np.array([h1, s1, v1])
  upper_color = np.array([h2, s2, v2])

  # Threshold na imagem HSV
  mask = cv2.inRange(hsv, lower_color, upper_color)

  # Bitwise-AND mask and original image
  res = cv2.bitwise_and(frame,frame, mask=mask)

  cv2.imshow('frame',frame)
  cv2.imshow('mask',mask)
  cv2.imshow('res',res)

  # Press Q on keyboard to  exit
  if cv2.waitKey(25) & 0xFF == ord('q'):
    break
 
  
# Closes all the frames
cv2.destroyAllWindows()
