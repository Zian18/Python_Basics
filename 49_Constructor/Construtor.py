
class Student:
    roll = ""
    gpa = ""


    def __init__(self, roll, gpa):
            self.roll = roll
            self.gpa = gpa


    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


rahim = Student(101, 3.75)
# rahim.set_value(101, 3.75)
rahim.display()


karim = Student(103, 3.85)
# karim.set_value(103, 3.85)
karim.display()
