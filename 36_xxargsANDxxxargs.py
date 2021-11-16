
# xxargs

# def student(id,name):
#     print(id,name)

def student(*details):
      print(details[0])


student(101, "Anis")
student(102, "Anis", 3.45)


def add(*numbers):
#    sum = num1 + num2

    sum = 0
    for num in numbers:
           sum = sum + num
print(sum)

add(10,20)
add(10,20,30)




# xxxargs


def student(**details):
  print(details["name"])


student(id=101, name = "Anis")