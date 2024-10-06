import cv2
import numpy

img = cv2.imread('gigapng.png')
arr = numpy.array(img)

cv2.rotate(arr,cv2.ROTATE_90_CLOCKWISE,arr)
cv2.namedWindow('giga')
cv2.imshow('giga',arr)
cv2.resizeWindow('giga',200,200)


cv2.waitKey(0)
