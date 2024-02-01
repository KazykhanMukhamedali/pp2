# The Syntax

'newlist = [expression for item in iterable if condition == True]'
# ex1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]

# ex2
newlist = [x for x in fruits]

# ex3
newlist = [x for x in range(10)]

# ex4
newlist = [x for x in range(10) if x < 5]

# ex5
newlist = [x.upper() for x in fruits]

# ex6
newlist = ['hello' for x in fruits]

# ex7
newlist = [x if x != "banana" else "orange" for x in fruits]