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

#######################################################################################################################################
#######################################################################################################################################
#######################################################################################################################################


def lower(f,x,ϵ=10**(-6),verbose=False):
    for i in [10,9,8,7,6,5]:
        if abs(f(x-ϵ)-f(x-ϵ/i**2))<10**(-i):
            if verbose==True:
                print("Uncertainly = ",10**(-i))
            return round(f(x-ϵ/i**2),i)
    return float("nan")
def upper(f,x,ϵ=10**(-6),verbose=False):
    for i in [10,9,8,7,6,5]:
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
            #print("numpy infinity")
            status='nope'
        elif f(x)!=f(x):
            #print("python nan")
            status='nope'
        else:
            status='yep'
    except (ZeroDivisionError,RuntimeWarning):
        print("python ZeroDivisionError")
        status='nope'

    if status=='yep':
        return f(x)
    elif abs(lower(f,x)-upper(f,x))<0.01:
        #print(abs(lower_limit(f,x)-upper_limit(f,x)))
        return np.mean([lower(f,x),upper(f,x)])
    else:
        print("The limit does not exists or cannot be determined.")
        return float("nan")


#def data_limit(x,y,p=100)
