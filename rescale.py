import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)


def rescaleFrame(frame, scale = 0.75):
    # will work with any image video and live video 


    width = int(frame.shape[1] * scale)
    heigth  = int(frame.shape[0] * scale)

    dimensions = (width, heigth)

    return cv.resize(frame, dimensions , interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

def changeRes(width, height):
    # will work with only live video 


    captuer.set(3,width)
    captuer.set(3,height)


captuer = cv.VideoCapture('Videos/dog.mp4')


while True : 
    isTrue, frame =  captuer.read()

    frame_resized = rescaleFrame(frame, scale = .2)



    cv.imshow('Video',frame)
    cv.imshow('Video Resized', frame_resized)


    if cv.waitKey(20) & 0xff == ord('d'):
        # if the letter d is pressed exit loop 
        break 

captuer.release()
cv.destroyAllWindows()