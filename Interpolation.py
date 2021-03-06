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

from .Core import *


#######################################################################################################################################
#######################################################################################################################################
class MethodError(Exception):
    pass
########################################################################################################################################
########################################################################################################################################


def full_lagrange(xdata,ydata,points=100):
    '''
    Returns two arrays, x and y=f(x), where f is the Lagrange Polynomial Interpolation for the collection of points (xdata, ydata).
    Naturally, the x and y arrays have resolution of points given by the points argument.
    It is not recommended to interpolate a lot of points on xdata and ydata;
    the optimal value of points is maybe 15 of 20 (x,y) pairs, maybe more.
    '''
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
    '''
    Reduce data before interpolation.
    '''
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



def Interpolate_Data(x,y,n=3,p=50):
    '''
    Interpolate the data.
    It is not useful to do it with functions, but is sort of eqivalent to Newton-Cotes formulas, but slower.
    It is not a good idea use a large n. Usually 2 < n < 7
    '''
    shapes_comparation(x,y)
    res=len(x)%n
    xglobal=[]
    yglobal=[]
    for i in range(len(x)-res):
        if i%(n-1)==0:
            a=full_lagrange(x[i:i+n],y[i:i+n],p)
            xglobal+=list(a[0])
            yglobal+=list(a[1])
    if res>1:
        a=full_lagrange(x[len(x)-res+1:len(x)],y[len(x)-res+1:len(x)],100)
        xglobal+=list(a[0])
        yglobal+=list(a[1])
    return (xglobal,yglobal)
