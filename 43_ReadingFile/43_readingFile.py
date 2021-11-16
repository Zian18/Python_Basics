from typing import Text


file = open("./student.txt", "r")
print(file.readable())
file.close()

file = open("./student.txt", "w")
print(file.writable())
file.close()

file = open("./student.txt", "r+") #readable and writeable
print(file.writable())
file.close()


file = open("./student.txt", "r+")
# print(file.writable())

text=file.read()

print(text)
size = len(text)
print(size)
file.close()

file = open("./student.txt", "r")
# print(file.readable())

text = file.readlines()[0]
print(text)
file.close()


for line in file:
    print(line)
