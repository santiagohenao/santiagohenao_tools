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
from . import Interpolation
from .Core import *
from .Limits import limit
from .Core import MethodError

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################

class Methods:
    def __init__(self):
        pass

    def Riemann(x,y,upper=False):
        '''
        Riemann sums calculator over the points (x,y)
        '''
        shapes_comparation(x,y)
        s=0
        if upper:
            for i in range(len(x)-1):
                s+=(x[i+1]-x[i])*y[i+1]
        else:
            for i in range(len(x)-1):
                s+=(x[i+1]-x[i])*y[i]
        return s

    def Trapezoid(x,y):
        '''
        Trapezoid-rule sums over (x,y)
        '''
        shapes_comparation(x,y)
        s=0
        for i in range(len(x)-1):
            s+=(y[i+1]+y[i])*(x[i+1]-x[i])/2
        return s



    def Simpson(x,y):
        '''
        Simpson rule. Newton-Cotes formula for parabolas.
        '''
        shapes_comparation(x,y)
        if np.std(np.array(x[1:])-np.array(x[:-1]))>10**(-7):
            raise ValueError("The Data must be evenly spaced.")
        s=0
        if len(x)&2==1:
            for i in range(len(x)):
                if i%2==0:
                    s+=(x[i+2]-x[i])/6 * (y[i]+4*y[i+1]+y[i+2])
        else:
            for i in range(len(x)-2):
                if i%2==0:
                    s+=(x[i+2]-x[i])/6 * (y[i]+4*y[i+1]+y[i+2])
            s+=(y[-1]+y[-2])*(x[-2]-x[-2])/2
        return s

#######################################################################################################################################

def DataIntegrate(x,y,method="Simpson",interpolation=1,points_for_interpolation=10):
    '''
    Main function to integrate data.
    '''
    methods=["RiemannUpper","RiemannLower","Trapezoid","Simpson"]
    xx=x;yy=y
    if not (method in methods):
        raise MethodError("This method is not aviable. Methods aviable are: %s" % methods)
    if interpolation>1:
        xx,yy=Interpolation.Interpolate_Data(x,y,interpolation,points_for_interpolation)
    if method==methods[0]:
        # RiemannUpper
        return Methods.Riemann(xx,yy,upper=True)
    elif method==methods[1]:
        # RiemannUpper
        return Methods.Riemann(xx,yy,upper=False)
    elif method==methods[2]:
        # Trapezoid
        return Methods.Trapezoid(xx,yy)
    elif method==methods[3]:
        # Simpson
        return Methods.Simpson(xx,yy)

def NIntegrate(f,a,b,n=300,method="Simpson",temperated=False,round_to=10):
    '''
    Main function to integrate functions with real limits.
    '''
    methods=["RiemannUpper","RiemannLower","Trapezoid","Simpson","MonteCarlo"]
    if not (method in methods):
        raise MethodError("This method is not aviable. Methods aviable are: %s" % methods)

    vf=np.vectorize(f)

    if method==methods[4]:
        # MonteCarlo
        in_d=0
        out_d=0
        h=max(vf(np.linspace(a,b,300)))
        d=min(vf(np.linspace(a,b,300)))
        p=0
        for i in range(n):
        	p=[np.random.uniform(a,b),np.random.uniform(d,h)]
        	if p[1]<=f(p[0]):
        		in_d+=1
        	else:
        		out_d+=1
        return round((in_d/(out_d+in_d))*(abs(h-d))*(b-a),round_to)
    xspace=np.linspace(a,b,n,dtype=np.float128)
    if temperated:
        image=generate_temperated(f,a,b)
    else:
        image=vf(xspace)
    if method==methods[0]:
        # RiemannUpper
        return round(Methods.Riemann(xspace,image,upper=True),round_to)
    elif method==methods[1]:
        # RiemannUpper
        return round(Methods.Riemann(xspace,image,upper=False),round_to)
    elif method==methods[2]:
        # Trapezoid
        return round(Methods.Trapezoid(xspace,image),round_to)
    elif method==methods[3]:
        # Simpson
        return round(Methods.Simpson(xspace,image),round_to)

def InfinityIntegrate(f,a,positive=True,method="Trapezoid",resolution=3.5):
    '''
    An attempt to integrate functions from a to infinity.
    '''
    g=np.vectorize(lambda t: f(1/t)/(t**2))
    h=np.vectorize(lambda t: f(-1/t)/(t**2))
    if positive:
        if a>=1:
            xspace=real_interval(omega=resolution,end=a)
            return DataIntegrate(xspace,g(xspace),method)
        elif a<1:
            xspace=real_interval(omega=resolution,end=1)
            return NIntegrate(f,a,1,1000000,method)+DataIntegrate(xspace,g(xspace),method)
