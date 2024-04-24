from functools import reduce
from operator import mul
import time
import math


# 1
def multiply_list(numbers):
    return reduce(mul, numbers)


numbers = [1, 2, 3, 4, 5]
print(multiply_list(numbers))


# 2
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower


s = "Hello World!"
upper, lower = count_case(s)
print(f"Upper case letters: {upper}, Lower case letters: {lower}")


# 3
def is_palindrome(s):
    return s == "".join(reversed(s))


print(is_palindrome("madam"))
print(is_palindrome("hello"))


# 4
def delayed_sqrt(n, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(n)


n = 25100
delay_ms = 2123
result = delayed_sqrt(n, delay_ms)
print(f"Square root of {n} after {delay_ms} milliseconds is {result}")


# 5

def are_all_true(elements):
    return all(elements)


print(are_all_true((True, True, True)))
print(are_all_true((True, False, True)))