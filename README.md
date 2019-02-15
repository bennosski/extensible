# extensible

A function decorator providing the flexibility to generalize functions to iterable arguments.

If no iterable arguments are present, extensible functions simply evaluate the function at the given arguments.

If an iterable argument is present, extensible functions return a list (nested if necessary) with the function evaluated at each of the values in the iterable argument while holding other non-iterable arguments constant. Iterable arguments can be lists, tuples, or objects such as numpy arrays.

If there are multiple iterable arguments, extensible functions will iterate through all the iterable arguments simultaneously.
```ruby
from extensible import extensible

@extensible()
def f(x, y):
  return x*y
  
f(1, 2)
f([1,2,3,4], 2)
f([1,2,3,4], [1,0,1,0])
```
will generate the output:
```
2
[2, 4, 6, 8]
[1, 0, 3, 0]
```

All iterable arguments are expected to be of the same length.

If iterable arguments are of different lengths (not recommended), iteration will end based on the shortest of the iterable arguments.

Arguments may be passed to the extensible decorator to specify the arguments over which the function should be made extensible. This is important in cases where some iterable arguments should not produce an interable outcome. The extensible decorator will only attempt to iterate over the specified arguments (if no arguments are specified then the extensible decorator will attempt to iterate over all iterable arguments). The arguments over which to iterate are specified as strings with the corresponding variable names of the arguments in the function being decorated.
```ruby
@extensible('x', 'y')
def f(x, y, z):
   return y*sum(z) if x>0 else 0

f([-1,1], [2,3], [1,1,1])
```
will generate the output:
```
[0, 9]
```
