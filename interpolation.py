#!/usr/bin/python3


'''
Interpolation tools
'''

try:
    import numpy as np
except ModuleNotFoundError:
    print("\"numpy\" not found. This module requires numpy")
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("\"matplotlib\" not found. This module requires matplotlib")

from .core import *


#######################################################################################################################################
#######################################################################################################################################
class MethodError(Exception):
    pass
########################################################################################################################################
########################################################################################################################################


def full_lagrange(xdata,ydata,points=100):
    if len(xdata)!=len(ydata):
        raise ValueError("xdata and ydata must be the same size, but have shapes %d and %d"%(len(xdata),len(ydata)))
    else:
        k=len(xdata)
    k=len(xdata)
    npx=np.array(xdata);npy=np.array(ydata)
    xglobal=np.linspace(npx[0],npx[-1],points)[:-1]
    yglobal=[]
    def L(q):
        rs=0
        for j in range(0,k):
            rp=1
            for i in exclude(j,k,0,1):
                    rp*=(q-npx[i])/(npx[j]-npx[i])
            rs+=npy[j]*rp
        return rs
    for w in xglobal:
        yglobal.append(L(w))
    return (xglobal,yglobal)

def reduced(xdata,ydata,points=100,reduction=1,method="random"):
    if len(xdata)!=len(ydata):
        raise ValueError("xdata and ydata must be the same size, but have shapes %d and %d"%(len(xdata),len(ydata)))
    zipped=list(zip(xdata,ydata))
    zippedred=reduce_list(zipped,reduction,method)
    k_=len(zippedred)
    xunzip=np.zeros(k_)
    yunzip=np.zeros(k_)
    for i in range(k_):
        xunzip[i]+=zippedred[i][0]
        yunzip[i]+=zippedred[i][1]
    return full_lagrange(xunzip,yunzip,points)
