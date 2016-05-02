"""
a for loop works like this:
1. it calls iter() on the object it's looping over
2. we get an iterator
3. the for loop continually next on the iterator object
4. until a stop iteration exception occurs

interface consists of a couple of methods
1. __iter__ on a container object
2. __next__ on an iterator object
^^^ both container and iterator can be the *same* object
"""

"""
our generator
when we call iter(...) on it... we should get back an iterator
what's an iterator? something that just implements __next__
"""
class CountToTen:
    def __init__(self):
        self.n = 1

    # oh hey... I'm also an iterator, I can return myself
    def __iter__(self):
        return self

    def __next__(self):
        # stop counting at 10 by raising exception
        if self.n > 10:
            raise StopIteration
        ret = self.n
        self.n += 1
        return ret

def count_to_ten():
    for i in range(1, 11):
        yield i


for i in count_to_ten():
    print(i)

"""
generator = CountToTen()
i = iter(generator)
print(next(i))
print(next(i))
print(next(i))
"""
"""
for n in CountToTen():
    print(n)
"""











