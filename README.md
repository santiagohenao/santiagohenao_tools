# santiagohenao_tools

This is the package file where I define useful tools for my class of Computational Methods.
All of this are programmed and written only by me, based on common mathematical/numerical methods to do certain things,
usually I do this methos first on Mathematica and then they are reprogrammed on Python3.
These files does not contain any code maded by third parties.

Santiago Henao Castellanos, Universidad de los Andes.

Go to examples fo better undestanding (soon). I'm bad explaining.

## core.py

Some common useful methods. Array manipulation/customization.

## D.py

Differentiation tools. Interpolation not included.

## Integration.py

Numerical Integration tools. For now, methods aviable are Riemann, Trapezoid, and Simpson Rule for data and functions.

MonteCarlo simple method is only aviable for functions on NIntegrate. DataIntegrate can interpolate the data before integration.

InfinityIntegrate seems to work... The optimal value for the resoluton seems to be "3.5", but resolution values lower than 3 dump my machine.

## Interpolation.py

Lagrange polynomial interpolation methods. Includes data reduction and partial interpolation for large Data, wich can be like Newton-Cotes formulas for unevelny spaced data.

## NewtonRhapson.py

Prospect of NewtonRhapson method.

## StringLength.py

Years ago I programmed an algorithm for finding the period of variable stars on Julia, and it works very well. FFT can easily find the period for evelny spaced data, but astronomical observations are all but evelny spaced on time.

The method is based on a kind of minimum-phase-entropy principle. It is described on [this paper](http://paperity.org/p/39394557/a-period-finding-method-for-sparse-randomly-spaced-observations-or-how-long-is-a-piece-of)
