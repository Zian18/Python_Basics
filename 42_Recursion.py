#Recursion is a process where function can call itself

def fact(n):
    if n ==1 :
        return 1
    else:
        return n*fact(n-1)

print(fact(5))