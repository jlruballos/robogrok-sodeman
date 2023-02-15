import numpy as np
import cv2

cap=cv2.VideoCapture(0)

cm_to_pixel=9.0/640.0

R180_X=[[1,0,0],[0,np.cos(np.pi),-np.sin(np.pi)],[0,np.sin(np.pi),np.cos(np.pi)]]
Rad=(-91.0/180.0)*np.pi
RZ=[[np.cos(Rad),-np.sin(Rad),0],[np.sin(Rad),np.cos(Rad),0],[0,0,1]]
R0_C=np.dot(R180_X,RZ)

d0_C=[[-2.5],[-0.2],[0]]

H0_C=np.concatenate((R0_C,d0_C),1)
H0_C=np.concatenate((H0_C,[[0,0,0,1]]),0)

R0_C=np.dot(R180_X,RZ)


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
    
    X_Location=column_location*cm_to_pixel

    row_sums=np.matrix(np.sum(BW,1))
    row_sums=row_sums.transpose()
    row_numbers=np.matrix(np.arange(480))
    row_mult=np.multiply(row_sums,row_numbers)
    total=np.sum(row_mult)
    total_total=np.sum(np.sum(BW))
    row_location=total/total_total
    
    Y_Location=row_location*cm_to_pixel

    PC=[[X_Location],[Y_Location],[0],[1]]

    P0=np.dot(H0_C,PC)

    X0=P0[0]
    Y0=P0[1]
    
    print(X0, Y0)
    
    k=cv2.waitKey(5)
    if k==27:
        break

cv2.destroyAllWindows()




print(frame)
