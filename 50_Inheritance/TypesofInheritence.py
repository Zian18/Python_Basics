# Hierarchical Inheritance
# Multi-Level Inheritance A to B to C

#Multiple Inheritance A to B and C to D


class A:
   
    def display1(self):
        print("I am inside A class")

class B(A):
        #display 1()
    def display2(self):
        print("I am inide in B class")

class C(B):
     #display 1()
      #display 2()
     def display3(self):
         super().display1()
         super().display2()
         print("I am inside C class")

ob1 = C()
# ob1.display1()
# ob1.display2()
ob1.display3()



#multilple
class A:
   
    def display(self):
        print("I am inside A class")

class B:
        #display 1()
    def display(self):
        print("I am inide in B class")

class C(A,B):
     #display 1()
      #display 2()
     def display(self):
         
         print("I am inside C class")

ob1 = C()
# ob1.display1()
# ob1.display2()
ob1.display()