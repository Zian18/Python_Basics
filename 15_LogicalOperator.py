# and, or , not

num1 = 20
num2 = 10
num3 = 80

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

#In case of 'and' all the conditions need to be meet.

#vowel a e i o u
#consonant

ch= 'w'

if ch =='a' or ch == 'e' or ch == 'i' or ch=='o' or ch=='u':
    print("Vowel")
else:
    print("Consonant")