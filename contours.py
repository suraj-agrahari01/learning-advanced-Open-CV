import cv2 as cv 
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)



blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank',blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)


# cv.CHAIN_APPROX_NONE means we will get all the coordinate where as cv.CHAIN_APPROX_simple gives only edges end 
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contour(s) found!')


ret, thresh = cv.threshold(gray, 125, 225, cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')


cv.drawContours(blank, contours, -1 , (0, 0 , 255), 2)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
