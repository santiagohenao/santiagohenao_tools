#!/usr/bin/python3


'''
Newton Rhapson Method
'''

try:
    import numpy as np
except ModuleNotFoundError:
    print("\"numpy\" not found. This module requires numpy")
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("\"matplotlib\" not found. This module requires matplotlib")


#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################


from .Core import *
from .D import ffd

def NR(f,t,h=10**(-9)):
    '''
    Single Newton-Rhapson iteration.
    '''
    return t-(f(t)/ffd(f,t,h))

def NewtonRaphson(f,seed=0,it=4,h=10**(-9)):
    r=seed
    for i in range(it):
        r=NR(f,r,h)
    while r==r+1 or r!=r:
        r=seed+np.random.uniform(-1,1,1)[0]
        for i in range(it):
            r=NR(f,r,h)
    return r
