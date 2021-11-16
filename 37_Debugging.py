def add(*numbers):
#    sum = num1 + num2

    sum = 0
    for num in numbers:
           sum = sum + num
    return sum

add(10,20)
print(add(10,20,30)