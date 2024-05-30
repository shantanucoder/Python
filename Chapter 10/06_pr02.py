#making a calculator for the bringing the value of  square, square root and cube....

import math

class Calculator:
    def __init__(self, num):
        self.num = num
        
    def square(self):
        return self.num * self.num

    def squareroot(self):
        return math.sqrt(self.num)

    def cube(self):
        return self.num * self.num * self.num
    
ActualNumber = Calculator(int(input("choose a number according to you :")))
print("The Chosen number is :-",ActualNumber.num)
print("The square of", ActualNumber.num, "is :-", ActualNumber.square())
print("The squareroot of", ActualNumber.num, "is :-",ActualNumber.squareroot())
print("The cube of", ActualNumber.num, "is :-",ActualNumber.cube())
