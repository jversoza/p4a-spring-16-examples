"""
for ch in "uriel":
    print(ch)

for ele in ["michelle", "uriel"]:
    print(ele)

for n in (1, 2, 3):
    print(n)

for i in range(5):
    print(i)

d = {'x':1, 'y':2}
for k, v in d.items():
    print(k, v)

f = open('/tmp/foo.txt', 'r')
for line in f:
    print(line)

when you use a for loop
you call built-in function called "iter" on the "container object" that you're looping over
"iter" ... gives back an "iterator object"
"""
class CountToTen:
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        ret = self.count
        self.count += 1
        return ret
        
"""
counter = CountToTen()
for i in counter:
    print(i)
"""

"""
generator is same thing... but it implements next and iter for you
by defining a function
yield - pause a function, give back value
call next on iterator.... and unpause function
"""
def infinite_count():
    i = -1
    while True:
        i += 1
        yield i


iterator = infinite_count()
print(next(iterator))
print(next(iterator))
print(next(iterator))















