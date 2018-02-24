#!/usr/bin/python3


'''
Some common functions, more or less independent to the other submodules.
'''

import time

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
    '''
    This make a "saw" function with the function f and a period T;
    makes the function repeats itself on intervals from b to b+T, with displacement a
    '''
    def p(x):
        return f((x-a)-T*np.floor((x-a)/T)+b)
    return p

def reduce_list(ls,it=1,method="random"):
    '''
    Delete elements froma a list. It is a good idea reduce pairs of lists with zip(l1,l2).
    If method is "random", each element will have a probability of 0.5 to be deleted.
    If as method you put an integer $n$, you will delete $n-1$ of each $n$ element.
    '''
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
    '''
    I miss Mathematica's Boole. Returns 0 if condition is false, 1 otherwise.
    It is great for exclude terms from a sum.
    '''
    if condition:
        return 0
    else:
        return 1

def exclude(ex,n,strt=0,stp=1):
    '''
    Gives an Integer iterator [strt,ex)U(ex,n), with stp as steps.
    '''
    return [q for q in range(strt,n,stp) if q!=ex]


def generate_temperated(func,start,end,δ=0.03,σ=0.05,density=1):
    '''
    Generates an x-array of pseudo adaptative distributed points from start to end.
    Where the derivative of the function func is too high on the surroindings of a point,
    then let's put nore points there. It is quite slow and not precise.
    '''
    from .D import ffd
    adap=[start]
    while adap[-1]<=end:
        ap=min([1/(density*np.mean([abs(ffd(func,q))**2 for q in np.linspace(-σ+adap[-1],σ+adap[-1],100)])),δ])
        adap.append(adap[-1]+ap)
    return adap

def shapes_comparation(x,y):
    '''
    Compare the shapes of the arrays x and y, and raise and error if they have different shapes.
    '''
    if np.shape(x)[0] != np.shape(y)[0]:
        raise ValueError("x and y must have same length, but have  {} and {}".format(np.shape(x)[0],np.shape(y)[0]))

def real_interval(omega=4,end=1):
    if omega<3:
        print("\033[91m DANGER: \033[0m a factor less than 3 will result in memory error.")
        print("It is \033[01m NOT \033[0m recommended to put 3 or less as factor here.")
        print("You have 5 seconds to Interrupt this kernel with Ctrl+C")
        i=5
        while i>0:
            print(i)
            time.sleep(1)
            i-=1
    δ=np.finfo(np.longfloat).eps
    a=[δ]
    c=2
    while a[-1]<end:
        a.append(c**omega*δ)
        c+=1
    return a
