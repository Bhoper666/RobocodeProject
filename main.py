import cv2

img = cv2.imread('gigapng.png')

img1 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img2 = cv2.rotate(img, cv2.ROTATE_180)
img3 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('giga90', img1)
cv2.imshow('giga180', img2)
cv2.imshow('giga270', img3)

cv2.waitKey(0)
