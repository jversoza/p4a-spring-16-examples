"""
1. determine a base case for which a value can be returned without recursion
2. find a way to continually simplify problem until base case is reached

* typically "persistent" state is passed back as a return value
* and passed on as an argument
"""


"""
count down to 0 (including)
count_down(start)
"""
def count_down(start):
    if start == 0:
        print(0)
    else:
        print(start)
        count_down(start - 1)
count_down(10)

"""
* build an array with elements based on specified range
* should act like range function
    * start at start
    * go up to but not include stop
    * increment by step
    * don't worry about negative step (ignore this case)
* implement recusively
arr_range(initial_array, start, stop, step)
"""
def arr_range(arr, start, stop, step):
    if start >= stop:
        return arr
    else:
        new_arr = arr_range(arr, start + step, stop, step)
        new_arr.insert(0, start)
        return new_arr

print(arr_range([], 0, 5, 1))
print(arr_range([], 2, 10, 2))

"""
* determine whether or not a string is a palindrome!
* (string is same forwards and backwards)
* (like racecar)
* (or anna)
* use recursion to do this

is_palindrome(some_string)
"""
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        same = s[0] == s[-1]
        return is_palindrome(s[1:-1]) if same else same

print('a', is_palindrome('a'))
print('ab', is_palindrome('ab'))
print('aba', is_palindrome('aba'))
print('aa', is_palindrome('aa'))
print('reacecar', is_palindrome('racecar'))
print('racecars', is_palindrome('racecars'))
print('racebar', is_palindrome('racebar'))
        


"""
* find largest number in list
* does not have to account for empty list (or give back None for empty list)
* do this recursively

get_max(list_of_numbers)
"""
def get_max(numbers):
    if len(numbers) <= 1:
        try:
            return numbers[0]
        except ZeroDivisionError:
            return None

    else:
        cur = numbers[0]
        other_max = get_max(numbers[1:])
        return cur if cur > other_max else other_max

print(get_max([4, 2, 1, 7, 5, 4]))
