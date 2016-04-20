class InfiniteAlphabet:
    START, END = 65, 90
    def __init__(self):
        self.code_point = InfiniteAlphabet.START

    def __iter__(self):
        return self

    def __next__(self):
        letter = chr(self.code_point)
        self.code_point += 1
        if self.code_point > InfiniteAlphabet.END:
            self.code_point = InfiniteAlphabet.START
        return letter

#for letter in InfiniteAlphabet():
#    print(letter)

def infinite_alphabet():
    START, END = 65, 90
    code_point = START
    while True:
        letter = chr(code_point)
        code_point += 1
        if code_point > END:
            code_point = START
        yield letter

infinity = infinite_alphabet()
print(next(infinity))
print(next(infinity))
#for letter in infinite_alphabet():
#    print(letter)
        
        


