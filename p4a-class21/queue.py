"""
classes and abstraction
contract between the programmer and the class that they're using

the class is going to define some "public" actions that you can do with the class
the programmers expects those actions / data to exist

(however, the underlying details can change, and the programmer doesn't have to know about that)
"""
"""
"it's a line"
first come first served
an ordered collection of elements, where the first element in is the first element out
fifo queue (first-in, first-out)
last in, first out... stack
priority queue
"""
"""
implement a fifo queue
"contract"
* whoever is using this class... expects these two methods
* (but nothing else)
enqueue
dequeue
linked lists is a common implementation

trust the programmer to do the right thing
inform the class user.. don't use this instance variable
oooor don't use this method

* convention is to use single _ before a method or a variable
  to indicate (don't use this!!!!)
* __ <-- prefix with two underscores
* mangles the name (so when you want to access it, you have to
  use _classname_variablename)
"""
class Queue:
    def __init__(self):
        self._elements = []

    def __str__(self):
        return str(self._elements)

    def enqueue(self, ele):
        self._elements.append(ele)

    def dequeue(self):
        return self._elements.pop(0)
        # val = self.elements[0]
        # del self.elements(0)
        # return val

"""
line_for_trendy_vegan_place = Queue()
line_for_trendy_vegan_place.dequeue()
line_for_trendy_vegan_place.enqueue('Joe')
line_for_trendy_vegan_place.enqueue('David')
print(line_for_trendy_vegan_place)
line_for_trendy_vegan_place.dequeue()
print(line_for_trendy_vegan_place)
line_for_trendy_vegan_place.elements.append('Alan')
"""

line_for_romeo = Queue()
line_for_423 = Queue()
"""
built in funciton called id
.... gives back a unique integer for an object
id... (in CPython) is the memory address
"""
a_long_line = line_for_romeo
print(id(line_for_romeo))
print(id(a_long_line))
print(id(line_for_423))
print(a_long_line.__class__)
print(line_for_423.__class__)
print(id(a_long_line.__class__))
print(id(line_for_423.__class__))





























