# also known as nested if statement

# if 7>9:
#     if 7>5:  inner if satement
#         print("Hi")

if 7>9:
    if 7>5:
        print("Hi")
    else:
        print("Goodbye")

num1 = 30
num2 = 20
num3 = -40

if num1 > num2:
    if num1 > num3: 
        print(num1)
    else:
        print(num3)

else:  
    if num2 >  num1:
        if num2 > num3:
            print(num2)
        else:
            print(num3)