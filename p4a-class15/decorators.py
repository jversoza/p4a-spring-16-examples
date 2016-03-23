def make_replacement(old_func):
    def new_func():
        res = old_func()
        res = res + " with pepperoni"
        return res
    return new_func

@make_replacement

def make_some_pizza():
    return 'pizza is made'

# make_some_pizza = make_replacement(make_some_pizza)

print(make_some_pizza())

def shout(old_func):
    def some_function(*args):
        return old_func(*args) + '!!!!!'
        
    return some_function

str = shout(str)

print(str(12))

import timeit
def timer(f):
    def new_f(*args):
        start = timeit.default_timer()
        ret = f(*args)
        end = timeit.default_timer()
        print("timing:", end - start)
        return ret

    return new_f

def cached(f):
    cache = {}
    def new_f(*args):
        if args in cache:
            print('cache hit', cache)
            return cache[args]
        else:
            res = f(*args)
            cache[args] = res
            return res
    return new_f

@timer
@cached
def fact(n):
    product = 1
    for i in range(1, n):
        product *= i
    return product

print(fact(3))
print(fact(8))
print(fact(8))
