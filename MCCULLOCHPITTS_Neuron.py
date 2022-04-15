#MCCULLOCH PITTS NEURON MODEL for implementing AND Gate
import numpy as np
#Data: AND inputs & output
X1=np.array([0, 0, 1, 1])
X2=np.array([0, 1, 0 ,1])
y=np.array([0, 0, 0, 1])
#Initialize Weights and Threshold
w1 = int(input("Weight w1 for input x1 :"))
w2 = int(input("Weight w2 for input x2 :"))
theta = int(input("Threshold (Theta)  :"))
#Summation
f=X1*w1+X2*w2
print (f)
#Activation
y_predict=(f>=theta).astype(int)
print ("Input values X1 and X2 :")
print(X1)
print(X2)
print ("Predicted output Y :")
print(y_predict)
if np.all(y==y_predict):
  print ('You have picked correct weights and threshold')
else:
  print ('change the weights and threshold')