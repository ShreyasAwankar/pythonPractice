class Dundrnot:
    def __init__(self, nam, sal):
        self.name = nam
        self.salary = sal

    def __add__(self, other):
        return self.salary + other.salary

emp1 = ('Sachin',  12000)
emp2 = ('Santosh', 15000)

print (emp1+emp2)

