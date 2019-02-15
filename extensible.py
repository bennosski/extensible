import types
import inspect

class extensible():

    '''
    If no iterable arguments are present, extensible functions simply evaluate the function at the given arguments.

    If iterable arguments are present, extensible functions return a list (nested if necessary) with the function evaluated at each of the values in the iterable arguments

    If there are multiple iterable arguments, extensible functions will iterate through all the iterable arguments simultaneously.

    All iterable arguments are expected to be of the same length
    
    If iterable arguments are of different lengths (not recommended), iteration will end based on the shortest of the iterable arguments.
    
    Arguments may be passed to the extensible decorator to specify over which arguments the functions should be made extensible. This is important in cases where some iterable arguments should not produce an interable outcome. The extensible decorator will only attempt to iterate over the specified arguments. The arguments are specified as strings with the corresponding variable names of the arguments in the function being decorated.
    
    
    '''

    """
    def __init__(self, f):
        self.f = f

    def _gen(self, x):
        while True: yield x
        
    def _iterator(self, x):
        try:
            return iter(x)
        except:
            return self._gen(x)

    def _arggenerator(self, iterators):
        while True:
            try:
                yield [next(i) for i in iterators]
            except:
                break

    def __call__(self, *args):
        iterators = [self._iterator(x) for x in args]

        if all([isinstance(i, types.GeneratorType) for i in iterators]):
            print('no iterable arguments')
            return self.f(*args)

        print('about to run extensibility')

        return [self.__call__(*a) for a in self._arggenerator(iterators)]
        

    """
    
    def __init__(self, *whichargs):
        self.whichargs = whichargs  

    def _gen(self, x):
        while True: yield x
        
    def _iterator(self, x):
        print('')
        #print(getattr(self.f, '__globals__'))
        #print([(a, self.var[a]==x) for a in self.whichargs])
        #if not any([self.var[a]==x for a in self.whichargs]):
        #    print('arg not found in specified args. do not iterate over')
        #    return self._gen(x)
        try:
            return iter(x)
        except:
            return self._gen(x)

    def _arggenerator(self, iterators):
        while True:
            try:
                yield [next(i) for i in iterators]
            except:
                break

    def __call__(self, f):
        self.f = f
        
        self.argnames = inspect.getfullargspec(self.f).args
        if self.whichargs:
            args_to_iterate = [arg in self.whichargs for arg in self.argnames]
        else:
            args_to_iterate = [True]*len(self.argnames)
        
        def wrapped_f(*args):

            iterators = [self._iterator(x) if args_to_iterate[i] else self._gen(x) for i,x in enumerate(args)]

            if all([isinstance(i, types.GeneratorType) for i in iterators]):
                return self.f(*args)

            return [wrapped_f(*a) for a in self._arggenerator(iterators)]
        
        return wrapped_f
       
