class Parent:
    a = 3

class Child1(Parent):
    b = 6

class Child2(Child1):
    c = 9


resultClass = Child2()

print(resultClass.a)
print(resultClass.b)
print(resultClass.c)
