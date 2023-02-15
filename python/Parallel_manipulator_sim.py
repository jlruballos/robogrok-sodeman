import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
plt.ion()
#plt.hold(False)
thetax=1.0
thetay=0.0

#Input the desired psotion and rotaion of the paltform
p=np.array([[5.0],[10.0]])
R=np.array([[1.0,0.0],[0.0,1.0]])

#Design variables
a1=np.array([[0.0],[0.0]])
a2=np.array([[10.0],[0.0]])

b1=np.array([[-1.0],[0.0]])
b2=np.array([[1.0],[0.0]])

i=0
while i<100:

    #Calculate outputs
    s1=p+np.dot(R,b1)-a1
    s2=p+np.dot(R,b2)-a2
    Length_s1=np.sqrt(s1[0]**2+s1[1]**2)
    Length_s2=np.sqrt(s2[0]**2+s2[1]**2)

    print("length s1 = ", Length_s1, "length s2 = ", Length_s2) 

    plt.plot([a1[0],s1[0]+a1[0],p[0],s2[0]+a2[0],a2[0]],[a1[1],s1[1]+a1[1],p[1],s2[1]+a2[1],a2[1]])
    plt.draw()
    plt.pause(0.01)
    i=i+1
    p[0]=p[0]+0.04
##    R[0][0]=R[0][0]-0.01
    R[1][0]=R[1][0]+0.01
    plt.clf()

plt.ioff()
plt.show()

