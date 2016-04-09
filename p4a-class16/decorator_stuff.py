"""
__name__ - name is the name of the module
or... it's the name of the currently running file which would be '__main__'

str.__name__
"""
print(str.__name__)
"""
decorate this function so that every time i call it
.... in addition to whatever the function does
.... "calling function" will be printed out
"""
from functools import wraps

def print_call(old_f):
    @wraps(old_f)
    def new_f(*args, **kwargs):
        print("calling function")
        res = old_f(*args, **kwargs)
        return res
    return new_f

@print_call
def foo():
    return 'bar'

print(foo())
print(foo.__name__)
decorated_print = print_call(print)
decorated_print('hello', 'world', sep='-')

"""
create a decorator called gather strings
...print out all of the return values that are strings
...from every call of the function
dstr = gather_strings(str)
dstr(5)
all strings: 5
dstr(2)
all strings: 5 2
"""
def gather_strings(old_f):
    all_strings = ''
    # cache = {}
    @wraps(old_f)
    def new_f(*args, **kwargs):
        nonlocal all_strings
        res = old_f(*args, **kwargs)
        if isinstance(res, str):
            all_strings = all_strings + ' ' + res
        print('all strings:', all_strings)
        return res
    return new_f

dstr = gather_strings(str)
dstr(5)
dstr(2)

"""
all_your_returns_are('....')

"""

def all_your_returns_are(obj):
    def decorator(old_f):
        def new_f(*args, **kwargs):
            res = old_f(*args, **kwargs)
            return obj
        return new_f
    return decorator


@all_your_returns_are('qux')
def bar():
    return 'baz'
print(bar())

@all_your_returns_are('blib')
def blubb():
    return 'blob'
print(blubb())









