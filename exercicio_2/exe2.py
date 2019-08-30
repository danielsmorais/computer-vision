import numpy as np
from cv2 import cv2 as cv

# Load an color image in grayscale
img = cv.imread('a1.jpg',0)





cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)