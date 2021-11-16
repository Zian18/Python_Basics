
from typing import Text


n = input("Enter a text of number : ")

list = n.split()  # 10 , 20 , 30 , 40
sum = 0

for num in list:
    sum = sum + int(sum)

    numOfWords = 0
    numOfLetters = 0
    numOfDigits = 0

    text = input("Enter a text of numbers: ")  # My name is 123

    for x in text:
        x = x.lower()
        if x >= 'a' and x <= 'z':
            numOfLetters = numOfLetters + 1

        elif x >= '0' and x <= '9':
          numOfDigits = numOfDigits + 1
        
        elif x == ' ':
          numOfWords = numOfWords + 1
print(numOfWords + 1)
print(numOfLetters)
print(numOfDigits)