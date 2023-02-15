import numpy as np

a1=5 #length of link a1 in cm
a2=2 #length of link a2 in cm
a3=3 #length of link a3 in cm
a4=4 #length of link a4 in cm

T1=30 #Theta 1 angle in degrees
T2=60 #Theta 2 angle in degrees

T1=(T1/180.0)*np.pi #Theta 1 in radians
T2=(T2/180.0)*np.pi #Theta 2 in radians

R0_1=[[np.cos(T1),0,np.sin(T1)],[np.sin(T1),0,-np.cos(T1)],[0,1,0]]
R1_2=[[np.cos(T2),-np.sin(T2),0],[np.sin(T2),np.cos(T2),0],[0,0,1]]

R0_2=np.dot(R0_1,R1_2)

#print(np.matrix(R0_1))
print ("\n")

d0_1=[[a2*np.cos(T1)],[a2*np.sin(T1)],[a1]]
d1_2=[[a3*np.cos(T2)],[a3*np.sin(T2)],[-a4]]

#print (np.matrix(d0_1))
print ("\n")

H0_1=np.concatenate((R0_1,d0_1),1)
H0_1=np.concatenate((H0_1,[[0,0,0,1]]),0)

#print (np.matrix(H0_1))

H1_2=np.concatenate((R1_2,d1_2),1)
H1_2=np.concatenate((H1_2,[[0,0,0,1]]),0)

H0_2=np.dot(H0_1,H1_2)

print(np.matrix(H0_2))


