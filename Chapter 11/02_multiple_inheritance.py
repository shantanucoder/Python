class Parent1:
    a = 3

class Parent2:
    b = 6

class Child(Parent1, Parent2):
    c = 9
resultClass = Child()

print(resultClass.a)
print(resultClass.b)
print(resultClass.c)

