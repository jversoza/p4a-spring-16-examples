Method Resolution Order and Super
=====

This is a summary of the following documents:

* [The Python 2.3 Method Resolution Order](https://www.python.org/download/releases/2.3/mro/) by Michele Simionato.
* [python.org's documentation on the built-in function, super](https://docs.python.org/3/library/functions.html#super)
* [The wonders of cooperative inheritance, or using super in Python 3](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/)
* [Super Considered Harmful](https://fuhm.org/super-harmful/)
* [Super Considered Super](http://www.artima.com/weblogs/viewpost.jsp?thread=281127)

In previous lectures we saw that:

1. Python supports multiple inheritance
    * which means that a subclass may inherit methods and properties from more than one parent class
    * the syntax for this is simply adding additional comma separated parent classes in the subclass definition:
        ```class Foo(Bar, Baz):
    pass
```
2. There's a special built-in function, `super()` that allows a subclass to access methods of its parent (its _super_) classes

Inheriting Methods / Overriding Methods 
-----

* when a subclass __inherits__ from a parent class, it inherits the methods of the parent class
    * so, a method may be invoked from an instance of subclass even if the subclass doesn't contain that method definition
    * example: class A (with method hello), class B is subclass of A.... so B inherits method hello
* a subclass may __override__ methods in the parent class by specifying a method of the same name
    * note that only the name has to be the same
    * __the arguments do not!?__ (that is the method _signature_ can differ)
    * example 1: add method w/ same name and same args to B
    * example 2: change args of B's hello...note that no arg version can no longer be called

In single inheritance (that is, when all of the classes in the inheritance chain only has one parent and / or one child), it's straightforward to determine what methods are overridden and inheritance. Just look for the presence or absence of  method names, starting with the subclass and going on through each _ancestor_ (parent) class!

However, with multiple inheritance, determining what methods are overridden and what methods are inherited can get a bit complicated. If there are multiple parents for a single subclass, in what order should we look at the classes to determine if a method exists? 

Let's get some definitions out of the way first
-----

Do determine where to find a method:

* we'll look at the class itself, as well as its ancestors from the nearest ancestor to the furthest
* this ordering of classes is called __linearlization__
* the __Method Resolution Order__ (MRO) is the set of rules that construct the linearization
* the phrase "the MRO of C" is synonymous with the _linearization_ of the class C.
* example: in single inheritance where A is a parent class of B, then the linearization (or MRO) of B is simply the list [B, A]; look at the subclass first... then the parent class

In fact, there's a method, ```mro``` that can be called on a class (the _actual class itself_) to reveal the order that the classes are visited in.

Multiple Inheritance
-----

Python uses an linearization algorithm called C3. (It was developed for another language called Dylan). As a developer, it's unlikely that you'll have to know how linearization works in simple cases, but if you have a complex hierarchy of classes with multiple inheritance, you'll have to know how this algorithm works.  (I should note, though... that a complex hierarchy of classes is itself a problem, and should probably be avoided!)

For multiple inheritance, the linearization of a subclass using the C3 algorithm results in the following properties:

* subclasses generally appear before parent classes
* parent class declaration order is preserved from left to right
* for all classes in an inheritance graph, the relative orderings guaranteed by 1 and 2 are preserved at all points in the graph
* also... not all possible inheritance graphs are legal! 

MRO / C3 Linearization Algorithm
-----

Simply put, the C3 linearization algorithm creates a linear / 1-D list of classes in a class hierarchy starting with a subclass. This ordering of classes determines what order the classes should be looked at in order to find a method.

In the following algorithm:

* C is a sublcass.
* L[C] is short for linearization of class C.
* B1... BN are the base / parent classes of class C.
* a series of concatenated letters is a list
* merge is an algorithm we'll describe as we go over the linearization algorithm
* head is the 1st element in a list of classes (the left most)
* tail is everything else

Briefly, this algorithm starts from the left most ancestor and goes depth first until there's a shared ancestor. So: depth first until shared ancestor.

1. the linearization of class C and its base classes
    * is the class C
    * plus the merge of the linearization of all of its base classes, and a list of all of its base classes
2. L[C] = C + merge(L[B1], L[B2] L[BN], B1B2..BN)
3. merge works by:
    * looking at the head of the linearization of the first base class
    * if that head doesn't exist in the tails of any of the other lists / linearizations
        * remove __all__ occurrences of that class in all of the other lists
        * and add that to the list outside of merge that starts with the original subclass, C
    * however, if the head does exist in the tails of other classes, stop processing the linearization for that particular base class and go on to the next base class linearization
    * repeat the process of determining if the head exists in other tails

Examples ... check the following by calling ```mro```:

* single inheritance
* 2 parents
* diamond
* diamond with depth first


super()
-----
So... what does super _actually_ do? It gives you the next class in the linearization of the subclass.

* Example: simple 3 class, multiplie inheritance where A and B are parents of C
* Example: call to super may be different depending on what's instantiated
* don't know at runtime which class / method combination will be called!!!

When using super
-----

* the method being called by super() needs to exist
* the caller and callee need to have a matching argument signature
* and every occurrence of the method needs to use super() (!!!)

This means that... you'll have problems when methods have the same name, but a different signature. To solve this:

* arbitrary number of arguments
* directly specify which one to call


Source Text from Referenced Documents
-----
Thus, the general rule is: always pass all arguments you received on to the super function, and, if classes can take differing arguments, always accept *args and **kwargs. This is shown in Example 1-3.

In a dynamic execution environment. This use case is unique to Python and is not found in statically compiled languages or languages that only support single inheritance. This makes it possible to implement “diamond diagrams” where multiple base classes implement the same method. Good design dictates that this method have the same calling signature in every case (because the order of calls is determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).
Never call super with anything but the exact arguments you received, unless you really know what you're doing.

Never use positional arguments in __init__ or __new__. Always use keyword args, and always call them as keywords, and always pass all keywords on to super.


