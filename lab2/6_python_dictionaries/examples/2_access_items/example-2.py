thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Get Keys


# ex1
x = thisdict.keys()

# ex2
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
