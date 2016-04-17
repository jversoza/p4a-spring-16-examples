"""
static
instance
"""

class Foo:
    # static variable
    qux = "QUXX"
    count = 0

    THIS_IS_CONSTANT = "YES IT IS!"

    def __init__(self):
        Foo.count += 1

    @staticmethod
    def bar():
        print("baz")

f = Foo()
"""
static method
"""
f.bar()
Foo.bar()
print(Foo.qux)








