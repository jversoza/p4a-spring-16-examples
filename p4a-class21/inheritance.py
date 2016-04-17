class Mammal:
    def mammal(self):
        print("I'm now mammelling")

    def __str__(self):
        return "I'm a mammal"


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def eat(self, food):
        print('eating ' + food)

    def __str__(self):
        return "{} {}".format(self.first, self.last)

"""
inheritance ... basing one off of another
parent ... is the class that will supply methods and variable
child ... is the class that inherits methods and variables

student inherits from person
...so student should be able eat...
"""
class Student(Person, Mammal):
    def __init__(self, first, last, netid):
        # somehow... call the parent constructor
        # super() ... that means... call the parent class method or constructor
        super().__init__(first, last)
        self.netid = netid

    """
    def __str__(self):
        return "{} {}, {}".format(self.first, self.last, self.netid)
    """

p = Person("Joe", "Versoza")
s = Student("Joe", "Versoza", 'jjv222')
print(s)

