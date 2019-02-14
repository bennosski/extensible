from extensible import extensible

@extensible
def f(x):
    return x**2

print('after decoration')

z = f(1)
print(z)


'''
x = [1,2,3,4]

def f(x):
    i = 0
    while i<10:
        yield x
        i += 1
        
g = f(1)

print(next(g))
print(next(g))
print(next(g))
print(next(g))

g = f(2)
print([x for x in g])


def g(i):
    while True:
        yield i

x = [1,2,3,4]
print(g(x))
print([y for y in g(x)])
'''

'''
it = iter([1,2,3,4])

#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))


def f(i):
    for x in i:
        yield x
        
g = f(it)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

'''

'''
its = [iter([1,2,3,4,5]), iter([1,2])]

def f(its):
    while True:
        try:
            yield [next(i) for i in its]
        except:
            break
            
g = f(its)
'''

'''
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''





'''
print(dir(f))
print(getattr(f, '__globals__'))

print('x in f')
print(getattr(f, '__globals__')['x']==x)

print('\nx dir')
print(dir(x))
print(getattr(x, '__str__'))
'''
