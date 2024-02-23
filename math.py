# ex 1
from math import pi
def converDegreetoRadian(degree):
    radians = degree * pi / 180
    return round(radians,6)
print("Radians:", converDegreetoRadian(int(input("Degree:"))))

# ex 2
def areaTrapesoid(height, firstb, secondb):
    area = (firstb + secondb) * height / 2
    return area
print("Area of Trapesoidal:", areaTrapesoid(int(input("Height:")), int(input("Firstb:")), int(input("Secondb:"))))

# ex 3
from math import tan, pi
def areaRegularPolygon(sides, length):
    area = int((sides * length ** 2) / (4 * tan(pi / sides)))
    return area

sides = int(input("Number of sides: "))
length = float(input("Length of sides: "))

print("Area:", areaRegularPolygon(sides, length))

# ex 4
def AreaOfParallelogram(length,height):
    area = length * height
    return area

print("Area:", AreaOfParallelogram(int(input("Length:")),int(input("Area:"))))

