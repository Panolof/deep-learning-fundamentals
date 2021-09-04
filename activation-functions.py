# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 20:56:35 2021

@author: Pano
"""
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))


def relu(x):
    return x if(x>=0) else 0



sig_Graph=[]
relu_Graph=[]

StartStop_X_Index=20
for i,val in enumerate(range(-StartStop_X_Index,StartStop_X_Index)):
    relu_Graph.append(relu(val))
    sig_Graph.append(sigmoid(val))
    
plt.subplot(2,1,1)    
plt.plot(sig_Graph)
plt.subplot(2,1,2)    
plt.plot(relu_Graph)    
    
