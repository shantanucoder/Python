class Employee:
     a = 8
     b = 4
     c = 6

     @classmethod
     def setAttrbts(cls, a, b, c):
          cls.a = a
          cls.b = b
          cls.c = c

emp = Employee()
print(Employee.a)
print(Employee.b)
print(Employee.c)

emp.setAttrbts(1, 2, 3) # after changing the attributes value in class

print(Employee.a)
print(Employee.b)
print(Employee.c)

