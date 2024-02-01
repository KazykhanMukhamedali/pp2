# Functions can Return a Boolean

# ex1
def myFunction() :
  return True

print(myFunction())

# ex2
def myFunction() :
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

# ex3
x = 200
print(isinstance(x, int))