class Animal:
    a = "Bark"

class Pet(Animal):
    b = "bark"

class Dog(Pet):
    c = "bark"

    @classmethod
    def BarkingStyle(cls, a, b, c):
        cls.a = a 
        cls.b = b
        cls.c = c

DogBark = Dog()

DogBark.BarkingStyle("Bark", "bark", "bark")

print("The dog is barking like this:")
print(Dog.a)
print(Dog.b)
print(Dog.c)