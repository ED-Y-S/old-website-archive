

# ZeroDivisionError:
# whenever you divide by 0

'''
12 / 0
12 / 0.0
12 // 0
12 % 0
'''

# AssertionError:
# whenever the `assert` function is called with a falsy argument

'''
assert(False)
assert(2 > 3)
assert([])
'''
def get_the_remainder(a,b): # all that assert is an exception checker whether if it is false
    assert(b>0)
    return a%b

# AttributeError:
# whenever the `object.function()` syntax is used, but `.function` is not applicable for `object`

'''
xs = [1, 2, 3]
xs.replace(2, 3) # replace() only works for str
s = 'hello '
s.append('world') # append() only works for list
'''

# IndexError:
# Whenever the [] notation is used is out of bounds for a *list*

'''
xs = [1, 2, 3]
xs[3]
'''

# KeyError:
# Whenever the [] notation is used is out of bounds for a *dictionary*

'''
d = { 'text': 'hello world' }
d['created_at']
'''

# NameError/UnboundLocalError:
# Whenever a variable is used that has not been defined

'''
example
d = { 'text': 'hello world' }
d[text]
def foo():
    example += 1
    return example
foo()
# NOTE:
# UnboundLocalError occurs only when the variable is used inside of a function,
# NameError occurs when the variable is used outside of a function. (Both are same, only that the prior one is in and calling a function)
# UnboundLocalError does not occur when the function is defined, but when the function is executed.
'''

# TypeError:
# There are several potential causes of this exception.

# 1. math operations are used on incompatible types

'''
'My age is ' + 35
None + 'test'
[1, 2, 3] + 4
'''

# NOTE:
# the following math operations are allowed
'''
4 + 0.4
'x' * 40   # but 'x' * 40.0 is not allowed
'''

# 2. len() is used on non-container types

'''
x = 5
len(x)
'''

# 3. subscripts are used on types that do not support them:

'''
x = 5
x[0]
xs = [1, 2, 3]
xs['test']
'''

# traceback = stack trace

################################################################################
# Dealing with stack traces

import requests
url = 'bad_url'


requests.get(url)


################################################################################
# catching error messages