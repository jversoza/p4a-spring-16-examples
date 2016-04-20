class A:
    def __init__(self):
        print("A.__init__")

class B(A):
    def __init__(self):
        print("B.__init__")
        print(super().__init__)
        super().__init__()
    
class C(A):
    def __init__(self):
        print("C.__init__")
        print(super().__init__)
        super().__init__()


class D(C):
    def __init__(self):
        print("D.__init__")
        print(super().__init__)
        super().__init__()

class E(D, B):
    def __init__(self):
        print("E.__init__")
        print(super().__init__)
        super().__init__()

print(E.mro())
e = E()
print(e)

"""
explicitly call constructor
use keyword args **kwargs
can't know what super() will give you - determined during runtime
"""
