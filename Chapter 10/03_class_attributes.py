# a very basic sample class
class Employee:
    name = "Shantanu"  #  a class attribute
    marks = 92
    Roll = 26
    Center = "The center is Delhi"

    def printObj(self):
        print(f"The name is {self.name}")

Employee.Center = "The center is Japan" # setting a class attribute for employee
Shantanu = Employee() # a BASIC OBJECT
sourav = Employee() # a BASIC OBJECT
print(Shantanu.name)
print(Shantanu.marks)
print(Shantanu.Roll)
print(Shantanu.Center)
Shantanu.printObj()
sourav.name = "Sourav"  #setting an instance attribute
print(sourav.name)
