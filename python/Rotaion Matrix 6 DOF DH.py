import numpy as np

d1=1
d2=1
d3=1

a1=1
a2=2
a3=3

T1=15 #Theta 1 angle in degrees
##T2=0 #Theta 2 angle in degrees
##T3=0 #Theta 3 angle in degrees
##T4=0 #Theta 4 angle in degrees
##T5=0 #Theta 5 angle in degrees
##T6=0 #Theta 6 angle in degrees

T1=(T1/180.0)*np.pi #Theta 1 in radians
##T2=(T2/180.0)*np.pi #Theta 2 in radians
##T3=(T3/180.0)*np.pi #Theta 3 in radians
##T4=(T4/180.0)*np.pi #Theta 4 in radians
##T5=(T5/180.0)*np.pi #Theta 5 in radians
##T6=(T6/180.0)*np.pi #Theta 6 in radians

M0_1=(90.0/180.0)*np.pi
PT=[[(195/180.0)*np.pi,(90.0/180.0)*np.pi,0,a1],
    [0,0,0,a2+a3+d2]]

i=0
H0_1=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
      [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
      [0,0,0,1]]
i=1
H1_2=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
      [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
      [0,0,0,1]]

##i=2
##H2_3=[[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],
##      [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
##      [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
##      [0,0,0,1]]

print ("0_1=")        
print (M0_1)
print ("PT=")        
print (np.matrix(PT))
print ("H0_1=")        
print (np.matrix(H0_1))
print ("H1_2=") 
print (np.matrix(H1_2))
##print ("H2_3=") 
##print (np.matrix(H2_3))

H0_2=np.dot(H0_1,H1_2)
##H0_3=np.dot(H0_2,H2_3)

print ("H0_2")
print (np.matrix(H0_2))
       
##R0_1=[[np.cos(T1),0,np.sin(T1)],[np.sin(T1),0,-np.cos(T1)],[0,1,0]]
##R1_2=[[np.cos(T2),-np.sin(T2),0],[np.sin(T2),np.cos(T2),0],[0,0,1]]
##R2_3=[[-np.sin(T3),0,np.cos(T3)],[np.cos(T3),0,np.sin(T3)],[0,1,0]]
##R3_4=[[np.cos(T4),0,-np.sin(T4)],[np.sin(T4),0,np.cos(T4)],[0,-1,0]]
##R4_5=[[-np.cos(T5),0,np.sin(T5)],[-np.sin(T5),0,-np.cos(T5)],[0,-1,0]]
##R5_6=[[np.cos(T6),-np.sin(T6),0],[np.sin(T6),np.cos(T6),0],[0,0,1]]
##
##R0_2=np.dot(R0_1,R1_2)
##R2_4=np.dot(R2_3,R3_4)
##R4_6=np.dot(R4_5,R5_6)
##
##R0_4=np.dot(R0_2,R2_4)
##R0_6=np.dot(R0_4,R4_6)
##
##print ('\nR0_1= ')
##print(np.matrix(R0_1))
##
##print ('\nR1_2= ')
##print(np.matrix(R1_2))
##
##print ('\nR2_3= ')
##print(np.matrix(R2_3))
##
##print ('\nR3_4= ')
##print(np.matrix(R3_4))
##
##print ('\nR4_5= ')
##print(np.matrix(R4_5))
##
##print ('\nR5_6= ')
##print(np.matrix(R5_6))
##
##print ('\nR0_6= ')
##print(np.matrix(R0_6))
