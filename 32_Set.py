num = {1,2,3,4,5,5} #curly braces used in set data and cannot put duplicate data
print(num)


num1 = {1,2,3,4,5}
num2 = set([4,5,6])

num2.add(7)
num2.remove(7)

print(num2)

print(7 in num2) #boolean result
print(4 in num2)


num1 = {1,2,3,4,5}
num2 = set([4,5,6,7])
print(num1 | num2) #union #it will show common number or duplicate number once
print(num1 & num2)  #intersenction
print(num1 - num2) #difference