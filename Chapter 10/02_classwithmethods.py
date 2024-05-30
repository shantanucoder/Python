# a very basic sample class
class Employee:
    name = "Shantanu"
    marks = 92
    Roll = 26
    Center = "Delhi"

    def printObj(self):
        print(f"The name is {self.name}")

    @staticmethod
    def greet():
         print("Good day!!")    

    @staticmethod
    def GetSalary():
         print("The salary of Shantanu Biswas is = Rs. 50,000")


Shantanu = Employee() # a BASIC OBJECT
print(Shantanu.Roll)
print(Shantanu.Center)
Shantanu.printObj()  # THE MEANING IS SAME AS - Employee.printObj(Shantanu)
Employee.printObj(Shantanu)
Employee.greet()
Shantanu.greet()
Employee.GetSalary()



