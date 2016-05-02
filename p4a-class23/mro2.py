"""
python supports multiple inheritance
it's non-trivial to determine which methods are overridden and which are inherited
this inheritance tree / graph can change *at runtime*

method resolution order - the way that python is order classes in class hierarchy to determine what's inherited and what's overridden

mro ... the mro of class C == the linearization of a class C

linearization of CBA

the algorithm is called C3 linearization (developed for another language called dylan)

depth first... until you reach a shared ancestor

C - subclass in question
B1, B2 ... BN ... base / super classes of C (ancestors of C)
L[C] <--- linearization of class C
merge() <--- we'll talk about this

CB1B2 <--- list of classes that i look at in order

linearization of C is... C first, then "merge" of linearization of all of its parent classes and all of its parent classes in a list

L[C] = C + merge(L[B1], L[B2]... L[BN], B1B2BN) 

head: 1st element (left-most)
tail: all remaining elements

merge: head (1st element) of the first (left-most) linearization
is the head in the tail of any of the other linearizations


what does super actually do?

super() calls a method on the superclass
.... that's not always the direct parent of the class in question


"""
"""
   A
  / \
 B   C
  \ /
   D
"""
"""
if you're using super
* use it for all methods of same name
* all methods with same name should have same signature

(or type error, passing too few or too many arguments)
"""
class A:
    def __init__(self):
        print("in A")
        super().__init__()

class B(A):
    def __init__(self):
        print("in B")
        super().__init__()

class C(A):
    def __init__(self):
        print("in C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("in D")
        super().__init__()

d = D()










