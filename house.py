import sys
import numpy as np


#import paddle
#import paddle.fluid as fluid
#import matplotlib.pyplot as plt
#import pandas as pd
#from paddle.fluid.contrib.trainer import *
#from paddle.fluid.contrib.inferencer import *
#%matplotlib inline

print("hello whale~~~now begin!")

data1=[6,7.5,8,0,1]
arr1=np.array(data1)
print(arr1)

data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr1.dtype)
print(arr2.dtype)

arr3=np.zeros(10)
print("arr3:\n",arr3)
arr4=np.zeros((3,6))
print("arr4:\n",arr4)

arr5=np.empty((2,3,2))
print("arr5:\n",arr5)














