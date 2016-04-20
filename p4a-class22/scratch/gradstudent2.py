class Person(object):
    def __init__(self, first_name, last_name, *args, **kwargs):
        self.first = first_name
        self.last = last_name

    def __str__(self):
        return "{} {}".format(self.first, self.last)

    def eat(self, food):
        print('eating ' + food)

class Student(Person):
    def __init__(self, first_name, last_name, netid):
        print(super().__init__)
        super().__init__(first_name, last_name, netid)
        self.netid = netid;

    def __str__(self):
        return "{} {}, {}".format(self.first, self.last, self.netid)

    def study(self):
        print("study")

class Teacher(Person):
    def __init__(self, first_name, last_name, *args, **kwargs):
        super().__init__(first_name, last_name, *args, **kwargs)

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

