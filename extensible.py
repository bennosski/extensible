import types

class extensible():

    def __init__(self, whichargs=None):
        self.whichargs = whichargs  
        self.f = f

    def _gen(self, x):
        while True: yield x
        
    def _iterator(self, x):
        if any([getattr(self.f, '__globals__')[a]==x for a in whichargs]):
            print('arg found in specified args')
            return self._gen(x)
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

        print('inside call')
        
        def wrapped_f(*args):

            print('decorator args')
            print(self.whichargs)
            print('f args')
            print(args)
            
            iterators = [self._iterator(x) for x in args]

            if all([isinstance(i, types.GeneratorType) for i in iterators]):
                print('no iterable arguments')
                return self.f(*args)

            print('about to run extensibility')

            return [self.f(*a) for a in self._arggenerator(iterators)]
        
        return wrapped_f
        
