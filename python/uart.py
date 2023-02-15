import serial

ser=serial.Serial()
ser.baudrate=9600
ser.port='COM3'
ser.open()

i=bytearray([255])
ser.write(i)
##a=[]
b=[]
c=[]
d=[]
##x=bytearray
y=bytearray()
j=0
##while(j<10):
##    a=([ser.read()])
##    print(a)
##    x=(a[0])
##    print(x)
##    c=10*x[0]
##    d.append(c)
##    j=j+1
while(j<200):
    a=([ser.read()])
    x=(a[0])
    b=([ser.read()])
    y=(b[0])
    c=x[0]*256+y[0]
    d.append(c)
    j=j+1
j=0
while(j<200):
    a=([ser.read()])
    x=(a[0])
    b=([ser.read()])
    y=(b[0])
    c=x[0]*256+y[0]
    d.append(c)
    j=j+1

ser.close()

file=open("Data.txt","w")

i=0
while(i<400):
    file.write("%d\n" % d[i])
    i=i+1

file.close()
