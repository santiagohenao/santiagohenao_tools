#!/usr/bin/python3


'''
Function limits tools
'''

try:
    import numpy as np
except ModuleNotFoundError:
    print("\"numpy\" not found. This module requires numpy")
try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("\"matplotlib\" not found. This module requires matplotlib")

import warnings
warnings.filterwarnings("ignore")

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################


def lower(f,x,ϵ=10**(-6),verbose=False):
    for i in [10,9,8,7,6]:
        print(i,abs(f(x-ϵ)-f(x-ϵ/i**2)),round(f(x-ϵ/i**2),i))
        if abs(f(x-ϵ)-f(x-ϵ/i**2))<10**(-i):
            if verbose==True:
                print("Uncertainly = ",10**(-i))
            return round(f(x-ϵ/i**2),i)
    return float("nan")
def upper(f,x,ϵ=10**(-6),verbose=False):
    for i in [10,9,8,7,6]:
        if abs(f(x+ϵ)-f(x+ϵ/i**2))<10**(-i):
            if verbose==True:
                print("Uncertainly = ",10**(-i))
            return round(f(x+ϵ/i**2),i)
    return float("nan")

def limit(f,x,ϵ=10**(-6)):
    status=''
    try:
        f(x)
        if f(x)==f(x)+1:
            status='nope'
        elif f(x)!=f(x):
            status='nope'
        else:
            status='yep'
    except (ZeroDivisionError,RuntimeWarning):
        #print("python ZeroDivisionError")
        status='nope'
    if status=='yep':
        return f(x)
    elif abs(lower(f,x)-upper(f,x))<0.01:
        #print(abs(lower_limit(f,x)-upper_limit(f,x)))
        return np.mean([lower(f,x),upper(f,x)])
    else:
        print("The limit does not exists or cannot be determined.")
        return float("nan")

#def improper(f,positive=True,ϵ=10**(-10),verbose=False):
#    if positive:
#        l=lower(lambda t: f(np.arctanh(t)),1,ϵ,verbose)
#        if l!=l:
#            l2=lower(lambda t: f(np.arctanh(t)),1,ϵ**2,verbose)
#            if l2!=l2:
#                l3=lower(lambda t: f(np.arctanh(t)),1,10**(-5),verbose)
#                if l3!=l3:
#                    print("Cannot find the limit. Best estimate:")
#                    return round(f(np.arctanh(ϵ-1)),10)
#                else:
#                    return l3
#            else:
#                return l2
#        else:
#            return l
#    else:
#        l=upper(lambda t: f(np.arctanh(t)),-1,ϵ,verbose)
#        if l!=l:
#            l2=upper(lambda t: f(np.arctanh(t)),-1,ϵ**2,verbose)
#            if l2!=l2:
#                l3=upper(lambda t: f(np.arctanh(t)),-1,10**(-5),verbose)
#                if l3!=l3:
#                    print("Cannot find the limit. Best estimate:")
#                    return f(np.arctanh(ϵ-1))
#                else:
#                    return l3
#            else:
#                return l2
#        else:
#            return l

#def data_limit(x,y,p=100)
