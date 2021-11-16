#1 + 2 + 3 + ....+ n

n= int(input("Enter the last number: "))

sum=0

for x in range(1,n+1,1): #form where will it start, how long will it run, difference form the previous number
    sum = sum + x 
print(sum)