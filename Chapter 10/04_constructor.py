# a very basic sample class

class Employee:
    name = "not known"
    center= "not known"

    def __init__(self, name, marks, center):
        self.name = name
        self.marks = marks 
        self.center = center 

    def printObj(self):
        print(f"The name is {self.name}")
        print(f"{self.name}'s marks is {self.marks}")
        print(f"{self.name}'s center is {self.center}")

@staticmethod
def greet():
    print("Good day!!")

shantanu = Employee("Shantanu Biswas", 90, "Delhi")
sourav = Employee("Sourav Biswas", 96, "Japan")
shantanu.printObj()
sourav.printObj()

