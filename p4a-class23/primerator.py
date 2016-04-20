

class PrimeGenerator:
    def __init__(self):
        self.i = 2

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.is_prime(self.i):
                n = self.i
                self.i += 1
                return n
            else:
                self.i += 1
        
    def is_prime(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

p = PrimeGenerator()
print(next(p))
print(next(p))
print(next(p))

for p in PrimeGenerator():
    print(p)
