thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Loop Through a Dictionary

# ex1
for x in thisdict:
    print(x)

# ex2
for x in thisdict:
    print(thisdict[x])

# ex3
for x in thisdict.values():
    print(x)

# ex4
for x in thisdict.keys():
    print(x)

# ex5
for x, y in thisdict.items():
    print(x, y)