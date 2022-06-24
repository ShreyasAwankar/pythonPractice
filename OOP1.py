class Employee:
    No_of_leaves = 22
    def __init__(self, nam, sal):
        self.name = nam
        self.salary = sal

    def __add__(self, other): #Dunder method (Starts and ends with "__" ) & used for operator overloadig.
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"({self.name}, {self.salary})"

    def __str__(self):
        return f"String method is preferred first in python in case printing obejects " \
               f"and you must call objects as shown in line 25 so as to execute repr"

Rohan = Employee("Rohan", 30000)
Harry = Employee("Harry", 40000)
print (Rohan+Harry)
print (Rohan/Harry)
print (Harry)
print (repr(Rohan))
