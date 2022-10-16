import cv2
import numpy as np
foto = cv2.imread("temperate-forest.jpg")
cv2.imshow("temperate-forest.jpg",foto)
cv2.waitKey()

B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]

fotogray = cv2.imread("temperate-forest.jpg",0)
cv2.imshow("temperate-forest.jpg",fotogray)
cv2.waitKey()

from matplotlib import pyplot as plt
import matplotlib.image as mpimg
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(fotogray, cmap = 'gray')
plt.show()

img_yuv = cv2.cvtColor(foto, cv2.COLORYU_BGR2V)
y, u, v = cv2.split(img_yuv)

cv2.imshow('y', y)
cv2.imshow('u', u)
cv2.imshow('v', v)
cv2.imshow("temperate-forest.jpg",img_yuv)
cv2.waitKey(0)




