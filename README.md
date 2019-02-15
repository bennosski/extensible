# extensible

A function decorator providing the flexibility to generalize functions to iterable arguments.

If no iterable arguments are present, extensible functions simply evaluate the function at the given arguments.

If an iterable argument is present, extensible functions return a list (nested if necessary) with the function evaluated at each of the values in the iterable arguments\
 while holding non-iterable arguments constant.

If there are multiple iterable arguments, extensible functions will iterate through all the iterable arguments simultaneously.

All iterable arguments are expected to be of the same length.

If iterable arguments are of different lengths (not recommended), iteration will end based on the shortest of the iterable arguments.

Arguments may be passed to the extensible decorator to specify the arguments over which the function should be made extensible. This is important in cases where some i\
terable arguments should not produce an interable outcome. The extensible decorator will only attempt to iterate over the specified arguments (if no arguments are specifie\
d then the extensible decorator will attempt to iterate over all iterable arguments). The arguments over which to iterate are specified as strings with the corresponding v\
ariable names of the arguments in the function being decorated.
