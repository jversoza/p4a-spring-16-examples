class A:
    def hello(self):
        print("Hello A")

class B(A):
    def hello(self, thing):
        print("Hello B", thing)

b = B()
b.hello()

