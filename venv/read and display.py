import cv2

image = cv2.imread('red roses.jpeg', 1)
print(image)
cv2.imshow('image', image)
cv2.waitKey(10000)
cv2.destroyAllWindows()
