class Student:
    minimum_attendance = 75 #class variable

    def __init__(self,nam, craft, sport, academics): #Constructor
        # Following three are instance varibles.
        self.name= nam
        self.craft_score = craft
        self.sport_score = sport
        self.academics_score = academics

    # @classmethod
    # def change_min_attendance(cls, new_min_attendance):
    #     cls.minimum_attendance = new_min_attendance

    @classmethod
    def splitter(cls,string): #class methods can be used as an alternative alternative constructor
        return cls(*string.split("-")) #As split will retun a list, '*' is used here for multiple string inputs for an object after splitting.

    def marks(self): #Instance method
        return f"Name of the Student is {self.name} and marks are: Crafts-{self.craft_score}," \
               f" Sport-{self.sport_score}, Academics- {self.academics_score}"


Shubham = Student("Shubham",75, 69, 84)
Kiran = Student("Kiran",65, 78, 61)
Mukesh = Student("Kiran",86, 64, 90)
Avinash = Student.splitter("Avinash-45-67-87") #Special string type input is provided here so as to make object with class method.

Mukesh.minimum_attendance = 60
# Student.minimum_attendance = 60


print(Shubham.minimum_attendance) #python always finds something in instance variables and if not found there then it will find in class variables.
print(Mukesh.academics_score)
print(Kiran.marks())
print (Avinash.marks())

print (Avinash.minimum_attendance)


