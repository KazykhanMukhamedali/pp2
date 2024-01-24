#example1
print("Hello")
print('Hello')

#example2
a = "Hello"
print(a)

#example3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#example4
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#example5
#Get the characters from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5])

#example6
#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

#example7
#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

#example8
'''
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):
'''
b = "Hello, World!"
print(b[-5:-2])

#example9
a = "Hello, World!"
print(a.upper())

#example10
a = "Hello, World!"
print(a.lower())

#exampl11
#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!

#example12
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#example13
#The split() method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#example14
a = "Hello"
b = "World"
c = a + b
print(c)

#example15
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#example16
#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#example16
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#example17
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#example18
txt = "We are the so-called \"Vikings\" from the north."

#example19
"""
capitalize()	    Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isascii()	        Returns True if all characters in the string are ascii characters
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()	    Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()	            Joins the elements of an iterable to the end of the string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was found
rindex()	        Searches the string for a specified value and returns the last position of where it was found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning
"""

