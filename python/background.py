import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while(1):

    _,frame=cap.read()

    gray_image1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('background',gray_image1)
    
    k=cv2.waitKey(5)
    if k==27:
        break

while(1):

    _,frame=cap.read()

    gray_image2=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('foreground',gray_image2)

    Difference=np.absolute(np.matrix(np.int16(gray_image1))-np.matrix(np.int16(gray_image2)))
    Difference[Difference>255]=255
    Difference=np.uint8(Difference)

    cv2.imshow('difference', Difference)

    BW=Difference
    BW[BW<=100]=0
    BW[BW>100]=1

    cv2.imshow('BW', BW)

    column_sums=np.matrix(np.sum(BW,0))
    column_numbers=np.matrix(np.arange(640))
    column_mult=np.multiply(column_sums,column_numbers)
    total=np.sum(column_mult)
    total_total=np.sum(np.sum(BW))
    column_location=total/total_total

    print(column_location)
    
    k=cv2.waitKey(5)
    if k==27:
        break

cv2.destroyAllWindows()




print(frame)
