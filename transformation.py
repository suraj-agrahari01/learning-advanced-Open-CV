#pylint:disable=no-member

import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# Translation means shifting across x and y axis 

def translate(img, x, y):
    # numnber of pixels to shift across x and y axis 

    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
        # rotate around center 
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    # sacling is not required so 1 is set 
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
# for clockwise use -ve value and for anti clockwise use +ve value 
# during rotation if there is no image then it will be black 


cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# for Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)
#  for shrinking use cv.INTER_ARIAL and if you are enlarging use  cv.INTER_CUBIC or cv.INTER_LINER


# Flipping
flip = cv.flip(img, -1)
# 0 means to tip vertically , 1 means flip   horizontally and -1 means both 
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)