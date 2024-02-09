# ex 1
def GramsToOunces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams = int(input("Grams:"))
print("Ounces:",GramsToOunces(grams))

# ex 2
def FarenheitToCelcius(F):
    C = (5/9) * (F - 32)
    return C

F = int(input("F:"))
print("C:", FarenheitToCelcius(F))

# ex 3
def solve(numheads, numlegs):
    r_cnt = 0
    c_cnt = 0
    if numlegs % 2 == 0 and numlegs > numheads:
        r_cnt = (numlegs // 2) - numheads
        c_cnt = numheads - r_cnt
    return r_cnt, c_cnt

numheads, numlegs = int(input("Heads:")), int(input("Legs:"))
print("Answer:",solve(numheads, numlegs))

# ex 4
import math
def filter_prime(lst):
    primes = []
    for x in lst:
        if x < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes

n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

print(filter_prime(numbers))

# ex 5
from itertools import permutations
def permutations(string):
    perms = [''.join(p) for p in permutations(string)]
    return perms

string = input()
print(permutations(string))

# ex 6
def reverser(string):
    string = string.split(" ")
    return string[::-1]

string = input()
print(reverser(string))

# ex 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = [1, 3, 3]
print(has_33(nums))

# ex 8
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2] == 7:
            return True
    return False

nums = [1,3,0,0,7,7,2]
print(spy_game(nums))

# ex 9
from math import pi
def volume(radius):
    volume = 4/3*pi*(radius**3)
    return volume

radius = int(input("Raduis:"))
print("Volume:", volume(radius))

# ex 10
def unique(lst1):
    lst2 = []
    for item in lst1:
        if item not in lst2:
            lst2.append(item)
    return lst2

lst1 = [1, 2, 2, 3, 4, 5, 5, 7, 7, 8]
print(unique(lst1))

# ex 11
def palindrome(string):
    s = []
    b = []
    for x in range(len(string)//2):
        s.append(string[x])
    for x in range(len(string//2), len(string)):
        b.append(string[x])
    if s == b[::-1]:
        return print("It is palindrome!")
    else:
        return print("It isnt palindrome")
    
string = input()
palindrome(string)

# ex 12
def histogram(nums):
    for n in nums:
        print('*' * n)

histogram([4, 9, 7])

# ex 13
import random
def guesser():
    global a
    a = random.randint(1,20)
name = input("Hello! What is your name?") # kbtu
guesser()
cnt = 0
while True:
    if cnt == 0:
        b = int(input(f"Well, {name}, I am thinking of a number between 1 and 20. Take a guess."))
    else:
        b = int(input())
    if a > b:
        print("Your guess is too low. Take a guess.")
        cnt += 1
    elif a < b:
        print("Your guess is too high. Take a guess.")
        cnt += 1
    elif a == b:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break

# ex 14

