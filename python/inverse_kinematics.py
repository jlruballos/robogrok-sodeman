import numpy as np

X=5.0
Y=0.0

Theta2=np.arctan2(Y,X)

R0_6=[[0.707,-0.707,0.0],
      [0.707,0.707,0.0],
      [0.0,0.0,1.0]]

R0_3=[[-np.sin(Theta2),0.0,np.cos(Theta2)],
      [np.cos(Theta2),0.0,np.sin(Theta2)],
      [0.0,1.0,0.0]]

invR0_3=np.linalg.inv(R0_3)

R3_6=np.dot(invR0_3,R0_6)

print ("R3_6= ",np.matrix(R3_6))

Theta5=np.arccos(R3_6[2][2])
print("Theta5= ", Theta5," radians")

Theta6=np.arccos(-R3_6[2][0]/np.sin(Theta5))
print("Theta6= ", Theta6," radians")

Theta4=np.arccos(R3_6[1][2]/np.sin(Theta5))
print("Theta4= ", Theta4," radians")

R3_6_Check=[[-np.sin(Theta4)*np.cos(Theta5)*np.cos(Theta6)-np.cos(Theta4)*np.sin(Theta6),np.sin(Theta4)*np.cos(Theta5)*np.sin(Theta6)-np.cos(Theta4)*np.cos(Theta6),-np.sin(Theta4)*np.sin(Theta5)],
            [np.cos(Theta4)*np.cos(Theta5)*np.cos(Theta6)-np.sin(Theta4)*np.sin(Theta6),-np.cos(Theta4)*np.cos(Theta5)*np.sin(Theta6)-np.sin(Theta4)*np.cos(Theta6),np.cos(Theta4)*np.sin(Theta5)],
            [-np.sin(Theta5)*np.cos(Theta6),np.sin(Theta5)*np.sin(Theta6)+np.cos(Theta5),np.cos(Theta5)]]

print ("R3_6_Check= ",np.matrix(R3_6_Check))
