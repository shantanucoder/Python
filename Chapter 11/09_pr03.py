#finding the salary increment value of an employee in  a company


class Employee:
    def __init__(self, salary, increment) -> None:
        self.salary = salary 
        self.increment = increment 

    @property
    def salaryAfterIncrement(self):
        return self.salary * (1 + self.increment) 

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.salary = value


emp1 = Employee(12000, 0.1)
print(emp1.salaryAfterIncrement)

emp1.salaryAfterIncrement = 11000
print(emp1.salaryAfterIncrement)
