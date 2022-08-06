import cv2
import numpy as np

image = cv2.imread("red roses.jpeg", 1)
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('image', image)
cv2.imshow('gaussian', gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
