import random

from random import randint  # alternative specific package

# for x in range(1, 6):

guessNumber = input("Enter your guess betwween 1 to 5 : ")
r4andomNumber = random.randint(1, 5)
randomNumber = random.random()*100

if guessNumber == randomNumber:
    print("You gave won")
else:
    print("You have lost")
    print("Random number was : ", randomNumber)
