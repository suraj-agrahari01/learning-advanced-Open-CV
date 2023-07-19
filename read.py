import cv2 as cv 

# img = cv.imread('Photos/cat_large.jpg')
# take image input 

# cv.imshow('Cat',img)
#dipslay img

# cv.waitKey(0)
#wiat for certain period of time before key is pressed 
# 0 means wiat for infinity time 
# if wait key absent it will just blink

captuer = cv.VideoCapture('Videos/dog.mp4')

# if you are using interger than it means you are using web cam or cammer 
# if you are using using ' ' thne it menas path name

while True : 
    isTrue, frame =  captuer.read()

    cv.imshow('Video',frame)


    if cv.waitKey(20) & 0xff == ord('d'):
        # if the letter d is pressed exit loop 
        break 

captuer.release()
cv.destroyAllWindows()


