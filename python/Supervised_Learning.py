import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import svm
from sklearn.neural_network import MLPClassifier

fig1=plt.figure()
ax1=fig1.add_subplot(111,projection='3d')

fig2=plt.figure()
ax2=fig2.add_subplot(111,projection='3d')

Training_Data=[[1,4,2],[1,3,2],[1,1,2],[1,1,1],[2,4,2],[2,4,1],[2,3,1],[2,1,1],[3,4,2],[3,4,1],[3,3,2],[3,3,1],[3,1,2]]
##Labels=[0,0,1,0,1,1,1,0,1,0,1,0,1]
Labels=[0,0,0,0,1,1,1,1,2,2,2,2,2]

Testing_Data=[[3,1,1],[1,4,1],[1,3,1],[2,3,2],[2,1,2]]

clf=svm.SVC()
Model=clf.fit(Training_Data,Labels)

Classification=clf.predict(Testing_Data)
print(Classification)

ax1.scatter([item[0] for item in Testing_Data],[item[1] for item in Testing_Data],[item[2] for item in Testing_Data], c=Classification,marker='x')
ax1.scatter([item[0] for item in Training_Data],[item[1] for item in Training_Data],[item[2] for item in Training_Data], c=Labels,marker='o')

ax1.set_xlabel('Color')
ax1.set_ylabel('Sides')
ax1.set_zlabel('Size')

clf=MLPClassifier(solver='lbfgs',alpha=1e-5, hidden_layer_sizes=(5,2), random_state=1)
Model=clf.fit(Training_Data,Labels)
Classification=clf.predict(Testing_Data)

ax2.scatter([item[0] for item in Testing_Data],[item[1] for item in Testing_Data],[item[2] for item in Testing_Data], c=Classification,marker='x')
ax2.scatter([item[0] for item in Training_Data],[item[1] for item in Training_Data],[item[2] for item in Training_Data], c=Labels,marker='o')

ax2.set_xlabel('Color')
ax2.set_ylabel('Sides')
ax2.set_zlabel('Size')


plt.show()
               
