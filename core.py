#!/usr/bin/python3


'''
Some common functions, more or less independent to the other submodules.
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
class MethodError(Exception):
    pass
#######################################################################################################################################
#######################################################################################################################################


def make_periodic(f,T,a=0,b=0):
    def p(x):
        return f((x-a)-T*np.floor((x-a)/T)+b)
    return p

def reduce_list(ls,it=1,method="random"):
    if type(method)!=int:
        if method!="random":
            raise MethodError("method must be \"random\" or an integer.")
    l=list(ls)
    rl=[]
    if method=="random":
        for i in range(len(l)):
            if np.random.choice([False, True]):
                rl.append(l[i])
        if it==1:
            return rl
        else:
            return reduce_list(rl,it-1)
    elif type(method)==int:
        for i in range(len(l)):
            if i%method==0:
                rl.append(l[i])
        if it==1:
            return rl
        else:
            return reduce_list(rl,it-1,method)


def boole(condition):
    if condition:
        return 0
    else:
        return 1

def exclude(ex,n,strt=0,stp=1):
	return [q for q in range(strt,n,stp) if q!=ex]

def ffd(func,x0,h=10**(-6)):
    d1=(func(x0+h)-func(x0))/h
    d2=(func(x0)-func(x0-h))/h
    return np.mean([d1,d2])

def generate_temperated(func,start,end,δ=0.03,σ=0.05,density=1):
    adap=[start]
    while adap[-1]<=end:
        ap=min([1/(density*np.mean([abs(ffd(func,q))**2 for q in np.linspace(-σ+adap[-1],σ+adap[-1],100)])),δ])
        adap.append(adap[-1]+ap)
    return adap
