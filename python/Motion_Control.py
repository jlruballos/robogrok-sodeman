import serial
import numpy as np
import time
import cv2
import matplotlib.pyplot as plt

ser=serial.Serial()
ser.baudrate=9600
ser.port='COM3'
ser.open()

##i=bytearray([np.uint8(150)]) #speed - steps per second
##ser.write(i)
##time.sleep(0.1)
##i=bytearray([np.uint8(1)]) #direction - 1 or 2
##ser.write(i)
##ser.close()

d_error=0
last_error=0
sum_error=0

cap=cv2.VideoCapture(0)

ErrorPlot=[]

while(1):

    _,frame=cap.read()

    red=np.matrix(frame[:,:,2])
    green=np.matrix(frame[:,:,1])
    blue=np.matrix(frame[:,:,0])

    red_only=np.int16(red)-np.int16(green)-np.int16(blue)

    red_only[red_only<0]=0
    red_only[red_only>255]=255

    red_only[red_only<50]=0
    red_only[red_only>=50]=255

    red_only=np.uint8(red_only)

    cv2.imshow('rgb', frame)
    cv2.imshow('red only', red_only)

    #thresholding to bw
    red_only[red_only>0]=1

    column_sums=np.matrix(np.sum(red_only,0))
    column_numbers=np.matrix(np.arange(640))
    column_mult=np.multiply(column_sums,column_numbers)
    total=np.sum(column_mult)
    total_total=np.sum(np.sum(red_only))
    column_location=total/total_total

    print(column_location)

    error=column_location-320

    ErrorPlot=np.append(ErrorPlot,error)
    
    Kp=1.0
    Kd=0.00
    Ki=0.00
    speed=Kp*error+Kd*d_error#+Ki*sum_error

    if (speed>150):
        speed=150
    if (speed<-150):
        speed=-150

    direction=1
    if (speed<0):
        speed=-speed
        direction=2
        
    i=bytearray([np.uint8(speed)]) #speed - steps per second
    ser.write(i)
    time.sleep(0.05)
    i=bytearray([np.uint8(direction)]) #direction - 1 or 2
    ser.write(i)
    time.sleep(0.05)

    d_error=(error-last_error)/0.1
    last_error=error
    sum_error=sum_error+(error*0.1)
    
    k=cv2.waitKey(5)
    if k==27:
        break

cv2.destroyAllWindows()

ser.close()

plt.figure(1)
plt.plot(ErrorPlot)
plt.show()


    

    
