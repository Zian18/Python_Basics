subjects = ["C", "C++", "JAVA", "Python", "BASIC"]

print(len(subjects))

subjects.append("JavaScript")
print (subjects)

subjects.insert(2,"Swift")
print(subjects)
subjects.remove("JAVA")
print(subjects)

subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

subjects.pop()
print(subjects)

subjects.clear()
print(subjects)

subjects2 = subjects.copy()
print(subjects)

pos= subjects.index(4)
print (subjects)


pos= subjects.count
print(subjects)
