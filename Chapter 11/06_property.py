class Employee:
     a = 8
     b = 4
     c = 6

     @classmethod
     def setAttrbts(cls, a, b, c):
          cls.a = a
          cls.b = b
          cls.c = c

     @property
     def length(self):
          return self.a
     
     @length.setter
     def length(self, value):
          self.a = value

emp = Employee()

emp.setAttrbts(1, 2, 3) # after changing the attributes value in class
print(emp.length)


emp.length = int(input("please enter the value:"))     #ENTER AN INTEGER HERE 
print(emp.length)
