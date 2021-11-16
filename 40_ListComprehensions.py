
num = [1,2,3,4,5]

#[expression for loop(variable) in list]

result = [x*x for x in num]


# result = list(map(lambda x:x*x,num))
print(result)

# result = list(filter(lambda x : x%2==0,num))
#for filter
result = [x for x in num if x%2==0]

print(result)