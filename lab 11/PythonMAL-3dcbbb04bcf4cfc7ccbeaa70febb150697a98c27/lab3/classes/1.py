import math
#1
class chetam:
    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input('Веедите че-то там\n')
    def printString(self):
        print(self.s)
#2-3
class shape:
    def __init__(self):
        self.area = 0
    def area(self):
        return self.area
class square(shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        self.area = self.length**2
        return self.area
class rectangle(shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width*self.length
#4
class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f'{self.x}, {self.y}')
    def move(self, x, y):
        self.x = input("Введите х: ")
        self.y = input("Введите у: ")
    def dist(self,x,y):
        return ((self.x - x)**2 + (self.y-y)**2)**(1/2)
#5
class account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, sum):
        self.balance+=sum
    def withdraw(self, sum):
        if sum>self.balance:
            print("malo denyag bomzhara")
        else:
            self.balance-=sum
#6
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True
def filter_list(list):
    return list(filter(lambda x: isPrime(x), list))