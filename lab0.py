# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:28:13 2019

@author: Danylo.Rusyn
"""

import cv2
camera = cv2.VideoCapture(0)
ret, image = camera.read()
cv2.imwrite('Photo.png', image)
camera.release()
cv2.imshow('My_Photo', image)
image = cv2.imread('Photo.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.line(image, (0, 0), (image.shape[1], image.shape[0]) , (255,0 , 190), 8)
cv2.rectangle(image, (12, 12), (365, 355), (0, 100, 255), 8)
cv2.imwrite('Photo.png', image)
cv2.imshow('My_Photo', image)
cv2.waitKey(0)
cv2.destroyAllWindows()