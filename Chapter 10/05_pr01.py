class Programmer:
    def __init__(self, name, language, Nationality):
         self.name = name 
         self.language = language 
         self.Nationality = Nationality 
    
    def printObj(self):
         print(f"The name is {self.name}")
         print(f"{self.name}'s good grasp on computer language is {self.language}")
         print(f"{self.name}'s nationality is {self.Nationality}")
         

shantanu = Programmer("Shantanu", "Python", "Japan")
sourav = Programmer("Sourav", "C++", "India")

print(shantanu.name)
shantanu.printObj()

print(sourav.name)
sourav.printObj()