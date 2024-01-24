#example1
x = 5
y = "John"
print(x)
print(y)

#example2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#example3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#example4
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#example5
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#example6
x = y = z = "Orange"
print(x)
print(y)
print(z)

#example7
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#example8
x = "Python is awesome"
print(x)

#example9
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#example10
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#example11
x = 5
y = "John"
print(x, y)

#example12
x = 5
y = 10
print(x + y)

#example13
#Variables that are created outside of a function (as in all of the examples above) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#example14
#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#example15
 #If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#example16
 #To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


