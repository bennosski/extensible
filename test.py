from extensible import extensible

@extensible()
def f(x, y):
    return x * y

print(f(2,3))           # evaluate the function as normal

print(f([1,2,3], 2))    # evaluate the function for each value in first arg, holding second arg constant

print(f([1,2,3], [1,2,3])) # evaluate the function while iterating over both args


@extensible('x')
def g(x, y):
    return x*sum(y)

print(g([1,2,3], [1,2,3]))  # evaluate the function while iterating over 'x' (do not iterate over 'y')







