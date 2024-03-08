# ex 1


# ex 2
s = "AAAaaaAAA"
cnt_upper = sum(1 for char in s if char.isupper())
cnt_lower = sum(1 for char in s if not char.isupper())
print(cnt_lower, cnt_upper)

# ex 3
def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while right >= left:
        if s[right] != s[left]:
            return False 
        right -= 1
        left += 1
    return True
print(isPalindrome("aba"))

# ex 4
import time
import math
def delayed_square_root(milliseconds):
    num = float(input("Enter a number:"))
    time.sleep(milliseconds / 1000)
    print("Square root:", math.sqrt(num))
    
milliseconds = int(input())
delayed_square_root(milliseconds)

# ex 5
def alltrue(tuple):
    return all(tuple)

tuple1 = (3==3, True, True, 4 > 3)

print(alltrue(tuple1))
