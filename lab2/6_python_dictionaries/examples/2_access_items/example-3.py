thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Get Values


# ex1
x = thisdict.values()

# ex2
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# ex3
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change