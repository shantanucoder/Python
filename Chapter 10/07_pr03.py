
class MyClass: # this is a class
    a = 9        # this is an attribute  

@staticmethod
def greet():
   print("Good day to you Mr. Shantanu Biswas")

greet() # I am callig a function 

obj = MyClass()    # checking the class attribute here  
print(obj.a)

obj.a = 0         # setting the instance attribute here 
print(obj.a)

MyClass.a = 10       # changing the class attribute here 
print(MyClass.a) 

