from extensible import extensible

@extensible()
def f(x, y):
    return x * y

print(f(2,3))           # evaluate the function as normal

print(f([1,2,3], 2))    # evaluate the function for each value in first arg, holding second arg constant

print(f([1,2,3], [1,2,3])) # evaluate the function while iterating over both args


@extensible('x', 'y')
def g(x, y, z):
    return y*sum(z) if x>0 else 0

print(g([-1,1], [2,3], [1,1,1]))  # evaluate the function while iterating over 'x' (do not iterate over 'y')


from numpy import *

print(f(ones([2,2]), ones([2,2])))







