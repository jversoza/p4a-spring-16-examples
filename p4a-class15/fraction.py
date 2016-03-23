class Fraction:
    def reduced(old_f):
        def new_f(*args):
            res = old_f(*args)
            return res.reduce()
        return new_f

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __str__(self):
        return "{} / {}".format(self.n, self.d)

    
    @staticmethod
    def gcf(a, b):
        for factor in range(min(a, b), 0, -1):
            if a % factor == 0 and b % factor == 0:
                return factor
        return 1

    def reduce(self):
        factor = Fraction.gcf(self.n, self.d)
        new_n = self.n // factor
        new_d = self.d // factor
        return Fraction(new_n, new_d)

    @reduced
    def add(self, other):
        new_d = self.d * other.d
        new_n = (self.d * other.n) + (other.d * self.n)
        ret = Fraction(new_n, new_d)
        return ret

    def __add__(self, other):
        return self.add(other)

    def __eq__(self, other):
        if self.n == other.n and self.d == other.d:
            return True
        else:
            return False

if __name__ == "__main__":
    a = Fraction(1, 4)
    b = Fraction(1, 4)
    c = Fraction(1, 2)
    print(a)
    print(a.add(b))
    print((a + b) == c)
























