"""
composition
----
has a --> part of a whole relationship
one object owns / contains --> another object
MultipleChoiceQuestion
Quiz --> has many MultipleChoiceQuestions
Survey --> has many MultipleChoiceQuestions
Code reuse FTW!!!!
self.attribute_name = other_object


ducktyping
-----
* regardless of type, if object responds to method
* that means that method can be invoked
* (this isn't the case in all languages, like Java for example)

polymoriphism
-----
* objects of different types behaving the same way
* in Python, ducktyping is (one)  mechanism for polymorphism ^^^
"""
"""
class Duck:
    def quack():
        print('quack')

class NotADuck:
    def quack():
        print('meow')

d = Duck()
n = NotADuck()
type(d) == type(n) # False
# but they can both quack

sometimes it's good practice to explicitly inherit from object
"""
class Person(object):
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def __str__(self):
        return "{} {}".format(self.first, self.last)

    def eat(self, food):
        print('eating ' + food)

class Student(Person):
    def __init__(self, first_name, last_name, netid):
        print(super().__init__)
        super().__init__(first_name, last_name)
        self.netid = netid;

    def __str__(self):
        return "{} {}, {}".format(self.first, self.last, self.netid)

    def study(self):
        print("study")

class Teacher(Person):
    def __init__(self, first_name, last_name, netid):
        super().__init__(first_name, last_name)

    def __str__(self):
        return "Professor {}".format(self.last)

    def teach(self):
        print("teaching")

# multiple inheritance is fine!
class GradStudent(Student, Teacher):
    def __init__(self, first_name, last_name, netid):
        print(super())
        super().__init__(first_name, last_name, netid)

print(GradStudent.mro())
g = GradStudent('Joe', 'Versoza', 'jjv222')
g.teach()
g.study()

"""
TODO: multiple inheritance and constructors
p = Person('Joe', 'Versoza')
s = Student('Joe', 'Versoza', 'jjv22')
t = Teacher('Joe', 'Versoza', 'jjv22')
print(p)
print(s)
print(t)
p.eat("pineapple")
s.eat("papaya")
"""
"""
inheritance vs composition
when???
it depends on the relationship you want
has a --> part of whole --> composition
is a --> one object can be considered as another --> inheritance
favor composition over inheritance
both ways to reuse code
sometimes you can use either...
"""
class Door:
    def __init__(self):
        self.status = "closed"

    def open(self):
        self.status = "open"

    def close(self):
        self.status = "closed"

    def is_open(self): # true or false
        return self.status == "open"

"""
class LockableDoor(Door):
    def __init__(self, locked):
        super().__init__()
        self.locked = locked

    def open(self):
        if not self.locked:
            super().open()
        else: 
            print("it's locked!")

d1 = Door()
d1.open()
print(d1.is_open())
d2 = LockableDoor(True)
d2.open()
print(d2.is_open())
"""


class LockableDoor():
    def __init__(self, locked):
        self.locked = locked
        self.door = Door()

    def open(self):
        if not self.locked:
            self.door.open()
        else:
            print("It's locked")

    def is_open(self):
        return self.door.is_open()

d2 = LockableDoor(True)
d2.open()
print(d2.is_open())








