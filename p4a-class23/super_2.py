class A:
    def __init__(self):
        print("A")
        super().__init__()

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B):
    def __init__(self):
        print("D")
        super().__init__()

class E(D, C):
    def __init__(self):
        print("E")
        super().__init__()

print("E\n-----")
e = E()
print()
print("B\n-----")
b = B()

