# ex 1
N = int(input("N:"))
squares = (x * x for x in range(1,N))
print(list(squares))

# ex 2
n = int(input("n:"))
evens = (x for x in range(1,n) if x % 2 == 0)
print(list(evens))

# ex 3
n = int(input("n:"))
divisibleby3 = (x for x in range(1,n) if x % 3 == 0 and x % 4 == 0)
print(list(divisibleby3))

# ex 4
def squares(a,b):
    while a <= b:
        yield a * a
        a += 1
a, b = int(input()), int(input())
nums = []
for x in squares(a, b):
    nums.append(x)
print(nums)

# ex 5
def down(a):
    while a >= 0:
        yield a
        a -= 1
a = int(input())
nums = []
for x in down(a):
    nums.append(x)
print(nums)