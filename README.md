# santiagohenao_tools

This is the package file where I define useful tools for my class of Computational Methods.
All of this are programmed and written only by me, based on common mathematical/numerical methods to do certain things,
usually I do this methos first on Mathematica and then they are reprogrammed on Python3.
These files does not contain any code maded by third parties.

Santiago Henao Castellanos, Universidad de los Andes.

Go to examples fo better undestanding. I'm bad explaining.

## core.py

Some common useful methods:

* ```make_periodic(f,T,a=0,b=0):```: This make a "saw" function with the function ```f``` and a period ```T```; makes the function repeats itself on intervals from ```b``` to ```b+TT```, with displacement ```a```. 

* ```reduce_list```: Delete elements froma a list. It is a good idea reduce pairs of lists with ```zip(l1,l2)```. If method is "random", each element will have a probability of 0.5 to be deleted. If as method you put an integer $n$, you will delete $n-1$ of each $n$ element.

* ```boole(condition):``` I miss Mathematica's Boole. Returns 0 if ```condition``` is false, 1 otherwise. It is great for exclude terms from a sum.

* ```exclude(ex,n,strt=0,stp=1):``` Gives an Integer iterator $[strt,ex)\cup(ex,n)$, with ```stp``` as steps.

* ```ffd(func,x0,h=10**(-6)):``` Fast Function derivative.

* ```generate_temperated(func,start,end,δ=0.03,σ=0.05,density=4):``` Generates an x-array of pseudo adaptative distributed points from ```start``` to ```end```. Where the derivative of the function ```func``` is too high on the surroindings of a point, then let's put nore points there. It is quite slow and not precise.


## diff.py

## NIntegrate.py

## DataIntegrate.py

## interpolation.py

* ```full_lagrange_interpolation(xdata,ydata,points=100):``` Returns two arrays, x and y=f(x), where f is the Lagrange Polynomial Interpolation for the collection of points xdata, ydata. Naturally, the x and y arrays have resolution of points given by the points argument. It is not recommended to interpolate a lot of points on xdata and ydata; the optimal value of points is maybe 15 of 20 (x,y) pairs, maybe more.

* ```reduced_interpolation(xdata,ydata,points=100,reduction=1,method="random"):``` If you have a big amount of data, you will maybe want to reduce it before interpolating.

## stringlength.py

