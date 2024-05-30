class Parent:
    a = 3
    def __init__(self) -> None:
        print("Parent")

class Child1(Parent):
    b = 6
    def __init__(self) -> None:
        super().__init__()
        print("Child1")

class Child2(Child1):
    c = 9
    def __init__(self) -> None:
        super().__init__()
        print("Child2")


resultClass = Child2()

print(resultClass.a)
print(resultClass.b)
print(resultClass.c)
