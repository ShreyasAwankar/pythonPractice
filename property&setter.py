class Person:
    def __init__(self,fnam,  lnam):
        self.first_name= fnam
        self.last_name= lnam
        # self.email= f"{self.first_name}.{self.last_name}@pycharm.com"

    @property #This is a property decorator. This will let us not provide '()' to print the eamil of any object.
    def email(self): #function
        if self.first_name==None or self.last_name==None:
            return "Email is not set please set it."
        return f"{self.first_name}.{self.last_name}@pycharm.com"

    @email.setter #to make a setter of a function, use the same name as of function.
    def email(self,string):
        name = string.split('@')[0]
        self.first_name = name.split('.')[0]
        self.last_name = name.split('.')[1]

    @email.deleter #This is a deleter, like a setter we need to define it using same name as of function .
    def email(self):
        self.first_name= None
        self.last_name= None



Rohan = Person("Roahan", "Patil") #Object
# print (Rohan.email)

Rohan.last_name= "Shinde"
# Rohan.email="This.that@pycharm.com" #this email got set because of the setter we made
# del Rohan.email
# Rohan.email= "ROHAN.shinde@gmail.com" #this email got set because of the setter we made

print (Rohan.email)
print (Rohan.first_name)
print (Rohan.last_name)

# import inspect
# print (inspect.getmembers(Rohan))


