class twoMethods:
    def __init__(self):
        self.input = ""
    def getString(self):
        self.input = input("Введите строку: ")
    def printString(self):
        self.input = print("Результат:", self.input.upper())
a = twoMethods()
a.getString()
a.printString()