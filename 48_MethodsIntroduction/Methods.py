
class Student:
    roll = ""
    gpa = ""


    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa


    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


rahim = Student()
rahim.set_value(101, 3.75)
rahim.display()

# print(f"Roll: {rahim.roll}, GPA: {rahim.gpa}")


karim = Student()
karim.set_value(103, 3.85)
karim.display()


# print(f"Roll: {karim.roll}, GPA: {karim.gpa}")
