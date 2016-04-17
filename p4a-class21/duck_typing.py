"""
if it looks like a duck and quacks like a duck
then it's a duck

if an object supports a method
it doesn't matter what type it is
you can still use it to call that method
"""
class Duck:
    def quack(self):
        print("quack")

class NotADuck:
    def quack(self):
        print("meow")

#d = Duck()
d = NotADuck()

for i in range(3):
    print(type(d))
    d.quack()


# code that writes a single random number to a file

class InMemoryFile:
    def __init__(self):
        self.s = ""

    def write(self, thing_to_write):
        self.s += thing_to_write
    
    def __str__(self):
        return self.s

import random
def write_random(file_obj):
    n = random.randint(1, 10)
    file_obj.write(str(n))


f = InMemoryFile()
write_random(f)
print(f)


"""
with open("/tmp/rando.txt", 'w') as f:
    write_random(f)
    f.close()
"""









