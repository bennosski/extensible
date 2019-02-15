import types
import inspect

class extensible():
    '''
    A function decorator adding flexibility for defining functions to work on both iterable and non-iterable arguments.

    If no iterable arguments are present, extensible functions simply evaluate the function at the given arguments.

    If iterable arguments are present, extensible functions return a list (nested if necessary) with the function evaluated at each of the values in the iterable arguments while holding non-iterable arguments constant.

    If there are multiple iterable arguments, extensible functions will iterate through all the iterable arguments simultaneously.

    All iterable arguments are expected to be of the same length.
    
    If iterable arguments are of different lengths (not recommended), iteration will end based on the shortest of the iterable arguments.
    
    Arguments may be passed to the extensible decorator to specify the arguments over which the function should be made extensible. This is important in cases where some iterable arguments should not produce an interable outcome. The extensible decorator will only attempt to iterate over the specified arguments (if no arguments are specified then the extensible decorator will attempt to iterate over all iterable arguments). The arguments over which to iterate are specified as strings with the corresponding variable names of the arguments in the function being decorated.
    '''
    
    def __init__(self, *whichargs):
        self.whichargs = whichargs  

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

    def __call__(self, f):        
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
       
