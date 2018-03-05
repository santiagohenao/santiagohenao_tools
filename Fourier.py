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
#######################################################################################################################################

Vround=np.vectorize(round)

def DiscreteTransform(freq,x,y):
    '''
    Calculate the value of the discrete Fourier transform for a dataset (x,y) at frquency freq.
    It works with unevenly spaced data as well.
    '''
    shapes_comparation(x,y)
    N=len(y)
    s=[(y[i])*np.exp(-2*np.pi*1j*freq*x[i]) for i in range(N)]
    return np.sum(s)


def Analysis(x,y,estimate,error=1,resolution=500):
    '''
    Execute a brief Fourier analysis of the data and visualize it.
    TODO: Return the maxima points.
    '''
    fs=np.linspace(estimate-error,estimate+error,resolution)
    ss=abs(np.array([DiscreteTransform(i,xs,ys) for i in fs]))

    fig,ax=plt.subplots(2,figsize=(20,15))
    ax[0].scatter(x,y,s=10,c='k')
    ax[0].grid("On")
    ax[0].set_xlabel("Data")
    ax[1].plot(fs,ss)
    ax[1].grid("On")
    ax[1].set_xlabel("Frequency")
    plt.show()

def Phaser(t,T,t_0=0):
    return ((t-t_0)/T)-(Vround((t-t_0)/T))
