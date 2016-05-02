"""
1. Python supports inheritance
    * one class, a subclass can inherit a bunch of methods from another class, a superclass
    * in the subclass, I could leave a method undefined.... aaaand... it'll still respond to that method call if the method exists in the superclass
    * in the case of single inheritance ^^^^ ... this is straightforward, but python also supports multiple inheritance
    * as a subclass... if I have method of the same name as the super class, I've overridden (my method takes precedence over super class method)
        * this works only by name
        * it doesn't matter what the arguments are!!! 
2. there's this built-in function called super... and it looks like it gives you access to the parent / super class
    * super().some_method <-- calls parent class some_method
    * again... easy to reason about in single inheritance chain
    * this is convoluted in multiple inheritance
"""
class A:
    def hello(self):
        print("hello from A")

    """
    def hello(self, name):
        print("hello 2 from A")

    def hello(self, *args):
        # switch based on # of args
        print("hello 2 from A")
    """


class B(A):
    def hello(self, name):
        print("hello from B", name)


b = B()
#b.hello("Joe")
b.hello()



















