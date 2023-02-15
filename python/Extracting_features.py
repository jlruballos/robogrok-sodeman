import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

cap=cv2.VideoCapture(0)

j=1
while(j<=2): #number of classes
    while (1):
        
        _,frame=cap.read()
        red=np.matrix(frame[:,:,2])
        green=np.matrix(frame[:,:,1])
        blue=np.matrix(frame[:,:,0])

        red_only=np.int16(red)-np.int16(green)-np.int16(blue)
        green_only=np.int16(green)-np.int16(red)
        blue_only=np.int16(blue)-np.int16(red)

        red_only[red_only<50]=0
        red_only[red_only>=50]=255

        green_only[green_only<1]=0
        green_only[green_only>=1]=255

        blue_only[blue_only<20]=0
        blue_only[blue_only>=20]=255

        red_only=np.uint8(red_only)
        green_only=np.uint8(green_only)
        blue_only=np.uint8(blue_only)

        all_only=red_only+green_only+blue_only
        
        mask=np.ones((5,5),np.uint8)
        opening=cv2.morphologyEx(all_only,cv2.MORPH_OPEN,mask)
        cv2.imshow('Masked Image',opening)
        
        _,labels=cv2.connectedComponents(opening,4)
        b=np.matrix(labels)

        i=1
        while (i<np.amax(labels) and i<10):
        
            Obj=b==i
            Obj=np.uint8(Obj)
            Obj[Obj>0]=255
            cv2.imshow('Object '+str(i),Obj)

            i=i+1
        
        cv2.imshow('Frame',frame)
        cv2.imshow('All Only',all_only)
        
        k=cv2.waitKey(5)
        if k==27:
            break

    cv2.destroyAllWindows()

    #Find RGB values of each object as the fiorst three features
    AvgRed=[]
    AvgBlue=[]
    AvgGreen=[]

    i=1
    while(i<=np.amax(labels)):
        Obj=b==i
        RedValues=np.array(Obj)*np.array(red)
        BlueValues=np.array(Obj)*np.array(blue)
        GreenValues=np.array(Obj)*np.array(green)

        size=np.sum(Obj)
        AvgSize=size/255.0
        AvgRed=np.append(AvgRed,np.sum(RedValues)/size)
        AvgGreen=np.append(AvgGreen,np.sum(BlueValues)/size)
        AvgBlue=np.append(AvgBlue,np.sum(GreenValues)/size)

        i=i+1
    if(j==1): #plot the class 1 point in blue
        ax.scatter(AvgRed,AvgBlue,AvgSize,c='b')
    if(j==2): #plot the class 2 point in red
        ax.scatter(AvgRed,AvgBlue,AvgSize,c='r')

    j=j+1

ax.set_xlabel('RedValue')
ax.set_ylabel('BlueValue')
ax.set_zlabel('GreenValue')

plt.show()
        





    
