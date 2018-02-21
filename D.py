#!/usr/bin/python3


'''
Function and data differentiation tools
'''

try:
    import numpy as np
except ModuleNotFoundError:
    print("\"numpy\" not found. This module requires numpy")
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("\"matplotlib\" not found. This module requires matplotlib")

from time import time
from . import interpolation
from .core import *
from .limits import limit


####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

def ffd(func,x0,h=10**(-6)):
    return (func(x0+h)-func(x0))/h

def ffd2(func,x0,h=10**(-6)):
    return (func(x0)-func(x0-h))/h

def array_diff(x,y):
    shapes_comparation(x,y)
    return np.concatenate((np.array(y[1:])-np.array(y[:-1]))/(np.array(x[1:])-np.array(x[:-1])),np.array((y[-1]-y[-2])/(x[-1]-x[-2])))

def DataDiff(x,y):
    shapes_comparation(x,y)
    d=[]
    for i in range(0,len(x)-1):
        d.append((y[i+1]-y[i])/(x[i+1]-x[i]))
    return d

#def limit_diff

#def diff
