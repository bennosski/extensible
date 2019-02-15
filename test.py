from extensible import extensible


'''
def extensible():
    def wrap(f):     
        
        def wrapped_f(*args):
            iterators = [_iterator(x) for x in args]

            if all([isinstance(i, types.GeneratorType) for i in iterators]):
                print('no iterable arguments')
                return self.f(*args)

            print('about to run extensibility')

            return [wrapped_f(*a) for a in self._arggenerator(iterators)]
        return wrapped_f
    return wrap
'''


@extensible('x', 'y')
def f(x, y):
    return x * y

print('after decoration')

#z = f([1,2,3], 2)
#print(z)

#z = f([1,2,3], 3)
#print(z)

z = f([[1,[2,6]],2,3,4], [[2,[3,0]],2])
print(z)



'''

class decorator_with_arguments(object):

    def __init__(self, *args):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()")
        self.args = args

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Inside __call__()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.args)
            return f(*args)
            print("After f(*args)")
        return wrapped_f

@decorator_with_arguments("hello")
def sayHello(a1, a2, a3, a4):
    return 'sayHello arguments: %s %s %s %s'%(a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
print(sayHello("say", "hello", "argument", "list"))
print('\n')
print("after first sayHello() call")
print(sayHello("a", "different", "set of", "arguments"))
print('\n')
print("after second sayHello() call")

'''

#z = f([1,2,3], [1,2,3])
#print(z)

#z = f([[1,2],2,3], [[1,3]])
#print(z)






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
