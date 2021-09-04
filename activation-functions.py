# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 20:56:35 2021

@author: Pano
"""
import numpy as np
import matplotlib.pyplot as plt
import time

def sigmoid(x):
    return 1/(1+np.exp(-x))

#####################################
##################################### FINDING OPTIMAL FUNCTION FOR RELU
#####################################
##################### Two different implementations of the RELU function

# More efficient - faster to implement
def relu1(x):
    return x if(x>0) else 0.0

# Less efficent - takes longer to implement
def relu2(x):
    return max(0.0,x)
#####################################
#######################
###############

def relu(x):
    return x if(x>0) else 0.0  
  
###############
#######################
#####################################

# This code below will run if this file is run directly. If we import this 
# script to another module, __name__ will change to the name of this file
# i.e. __name__ will then be equal to "activation-functions.py"
# (1) We compare times by testing the relu functions relu1 and relu2 
# (2) Plots are made of either functions 


if __name__=="__main__":
    def timeComparison(func,rangeOfValues):
        startTime=time.time()
        for i in range(-rangeOfValues,rangeOfValues):
            a=func(i)
        stopTime=time.time()
        time_relu=stopTime-startTime
        return time_relu    

    # from minus rangeOfVal to positive rangeOfVal
    rangeOfVal=10000000
    time_relu1=timeComparison(relu1,rangeOfVal)
    time_relu2=timeComparison(relu2,rangeOfVal)
    
    #####################################
    print("____________________________________")
    print("Time comparison of Relu 1 vs Relu 2")
    print("Relu 1",time_relu1)
    print("Relu 2",time_relu2)
    print("____________________________________")
    #####################################
    if (time_relu1>time_relu2):
        relu_final=relu2
        print("Relu 2 (using max) is the faster implementation\n")
    else:
        relu_final=relu1
        print("Relu 1 (using conditional logic) is the faster implementation\n")
    ### Test that the function works
    startTime=time.time()
    for i in range(-rangeOfVal,rangeOfVal):
        a=relu_final(i)
    stopTime=time.time()
    time_relu=stopTime-startTime
    #####################################
    print("Time comparison of optimal relu")
    print("Relu time",time_relu)    
        
    #####################################
    ##################################### PLOTTING SOME GRAPHS
    #####################################
    
    sig_Graph=[]
    relu_Graph=[]
    x_val=[]    
    StartStop_X_Index=20

    for i,val in enumerate(range(-StartStop_X_Index,StartStop_X_Index)):
        relu_Graph.append(relu(val))
        sig_Graph.append(sigmoid(val))
        x_val.append(val)
        
    plt.subplot(2,1,1)    
    plt.title("Sigmoid Funtion")
    plt.xlabel("x axis (inputs)")
    plt.ylabel("y axis (output range)")
    plt.plot(x_val,sig_Graph)
    plt.subplot(2,1,2)  
    plt.title("Relu Funtion")    
    plt.xlabel("x axis (inputs)")
    plt.ylabel("y axis (output range)")    
    plt.plot(x_val,relu_Graph)    
    plt.show()
        




