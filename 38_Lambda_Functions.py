
# def calculate (a,b):
#     return a*a + 2*a*b + b*b

#lambda parameter : expression

(lambda a,b : a*a + 2*a*b + b*b)

print((lambda a,b : a*a + 2*a*b + b*b) (2,3))

a = print((lambda a,b : a*a + 2*a*b + b*b) (2,3))

print (a)


def cube(x):
    return x*x*x
a = (lambda x : x*x*x) (2)

print(a)