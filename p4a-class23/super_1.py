
class A:
    def __init__(self):
        super().__init__()
        print("in A")

class B:
    def __init__(self):
        super().__init__()
        print("in B")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("in C")


a = A()
print()

c = C()


