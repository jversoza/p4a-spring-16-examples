def product(*args):
    res = 1
    for n in args:
        res *= n
    return res

print(product(1, 2))
print(product(1, 2, 3))

def f(*args):
    # using args within the function body... gives us a tuple
    # representing all arguments
    print(args)

    # when prefixed with a star... a tuple is unpacked into separate arguments
    print(*args)

f("hello", "goodbye")

t = (1, 2, 3)
print(t)
print(*t)
words = ['foo', 'bar', 'baz']
print(*words)
