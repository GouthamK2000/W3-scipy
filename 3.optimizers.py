# Optimizers in SciPy

# Optimizers are a set of procedures defined in SciPy that either find the minimum value of a function, or the root of an equation.

# Optimizing Functions
# Essentially, all of the algorithms in Machine Learning are nothing more than a complex equation that needs to be minimized with the help of given data.

# Roots of an Equation
# NumPy is capable of finding roots for polynomials and linear equations, but it can not find roots for non linear equations, like this one:

# x + cos(x)

# For that you can use SciPy's optimze.root function.

# This function takes two required arguments:

# fun - a function representing an equation.

# x0 - an initial guess for the root.

# The function returns an object with information regarding the solution.

# The actual solution is given under attribute x of the returned object:

#Case-1- Roots of non-linear equations

from scipy.optimize import root
from math import cos

def eqn(x):
    return x+cos(x)

myroot=root(eqn,0)
print(myroot.x)

#Output : 
# [-0.73908513]
