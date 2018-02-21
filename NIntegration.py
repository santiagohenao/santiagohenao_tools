#!/usr/bin/python3


'''
Function and data integration tools
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

from .core import MethodError

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################

class Methods:
    def __init__(self):
        pass
    def Riemann(x,y,upper=False):
        shapes_comparation(x,y)
        s=0
        if upper:
            for i in range(len(x)-1):
                s+=(x[i+1]-x[i])*y[i+1]
        if not upper:
            for i in range(len(x)-1):
                s+=(x[i+1]-x[i])*y[i]
        return s
    def Trapezoid(x,y):
        shapes_comparation(x,y)
        s=0
        for i in range(len(x)-1):
            s+=(y[i+1]+y[i])*(x[i+1]-x[i])/2
        return s
    def Interpolate_Data(x,y,n=3,p=50):
        '''
        It is not a good idea use a large n. Usually 2 < n < 7
        Simpson method when n = 3
        '''
        shapes_comparation(x,y)
        res=len(x)%n
        xglobal=[]
        yglobal=[]
        for i in range(len(x)-res):
            if i%(n-1)==0:
                a=interpolation.full_lagrange(x[i:i+n],y[i:i+n],p)
                xglobal+=list(a[0])
                yglobal+=list(a[1])
        if res>0:
            a=interpolation.full_lagrange(x[len(x)-res:len(x)],y[len(x)-res:len(x)],p)
            xglobal+=list(a[0])
            yglobal+=list(a[1])
        return (xglobal,yglobal)






    #def MonteCarlo

    #def temperated

    #def polynomial







#def DataIntegrate

#def NIntegrate

#def improper_bounds
