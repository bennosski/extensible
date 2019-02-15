from extensible import extensible

@extensible('x', 'y')
def f(x, y):
    return x * y

print(f(2,3))

print(f([1,2,3], 2))

print(f([1,2,3], [1,2,3]))



