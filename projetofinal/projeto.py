import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

cap = cv2.VideoCapture('video.mp4')

#f= open("dados.txt","w+")

# --------------------------------------------------------------------
# ------------------------ FILTRO DE KALMAN --------------------------
# --------------------------------------------------------------------
# taxa de amostragem
dt = 1/30.0

# Vetor de estados
# X = [x, y, vx, vy])
X = np.array([[546], [223], [0], [0]])

# Matriz de transicao
# Xk+1 = PHI*Xk + u
PHI = np.array([[1, 0, dt, 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0, 1]])

# Variancia da estimativa
# Inicialmente nula pois a condicao inicial eh conhecida
P = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

# Variancia do ruido dinamico
Q = np.array([[1.5**2, 0, 0, 0], [0, 1.5**2, 0, 0], [0, 0, 1.5**2, 0], [0, 0, 0, 1.5**2]])*60.0

# Matriz de medicao
H = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])
# Variancia do ruido de medicao
R = np.array([[133**2, 0], [0, 75**2]])*0.05

# Dados filtrados
# 2 colunas = x y
filtr = np.zeros((546, 2), dtype=np.int)

# --------------------------------------------------------------------

  
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    #conversao
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #definicao do range
    lower_color = np.array([0, 93, 126])
    upper_color = np.array([65, 255, 255])

    # Threshold na imagem HSV
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask=mask)

    # Calcula os contornos para calcular os momentos
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    c = max(contours, key = cv2.contourArea)
    M = cv2.moments(c)
    
    # calcula as coordenadas do centro da regiao
    if M["m00"] != 0:
      cX = int(M["m10"] / M["m00"])
      cY = int(M["m01"] / M["m00"])
    else:
      cX, cY = 0.0, 0.0

    # --------------------------------------------------------------------
    # ------------------------ FILTRO DE KALMAN --------------------------
    # --------------------------------------------------------------------
    # Fase de predicao
    X = np.mat(PHI)*np.mat(X)
    P = np.mat(PHI)*np.mat(P)*np.transpose(PHI) + np.mat(Q)

    # Medicao
    Y = np.array([[cX],[cY]]);

    # Fase de correcao
    K = np.mat(P)*np.transpose(H)*np.linalg.inv(np.mat(H)*np.mat(P)*np.transpose(H) + np.mat(R))
    X = np.mat(X) + np.mat(K)*(np.mat(Y)-np.mat(H)*np.mat(X));
    P = np.mat(P) - np.mat(K)*np.mat(H)*np.mat(P);

    # --------------------------------------------------------------------

    text = "("+str(cX)+","+str(cY)+")" + " - " + "("+str(int(X[0])).strip('[]')+","+str(int(X[1])).strip('[]')+")"
    cv2.putText(frame, text, (30, 450),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.circle(frame, (cX, cY), 4, (255, 0, 0), -1)
  
    # display the image
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    #f.write(str(cX)+" "+str(cY)+" "+str(X[0]).strip('[]')+" "+str(X[1]).strip('[]')+"\n")
 
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
