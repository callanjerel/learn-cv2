#code by callanjerel, basic cv2 copy and pasting, as well as printing
import cv2
import random


img = cv2.imread('assets/logo.jpg', 1)

tag = img[20:70, 20:70]
img[70:120, 70:120] = tag

print(img)
print(img.size)
print(type(img))

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()