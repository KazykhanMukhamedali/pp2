class Shape:
    def __init__(self):
        self.area = 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def getLength(self):
        self.length = int(input("Type length:"))

    def calculateArea(self):
        self.area = self.length * self.length
        return self.area
a = Square(0)
a.getLength()
print("Area is equal", a.calculateArea())