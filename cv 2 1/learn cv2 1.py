import cv2

#-1, cv2.IMREAD_COLOR: loads color, ignores transparency
#0, cv2.IMREAD_GRAYSCALE: loads image in grayscale mode
#1, cv2.IMREAD_UNCHANGED: loads image as is (including transparency)

img = cv2.imread('assets/logo.jpg', 1)
img = cv2.resize(img, (0,0), fx=1, fy=1)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('assets/new_img.jpg', img)

cv2.imshow('the image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()