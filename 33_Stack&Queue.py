#Stack

books = []

books.append ("Learn C")
books.append ("Learn C++")
books.append ("JavaScript")
books.append ("Python")

print(books)

books.pop()  #LIFO
print(books)

books.pop()
print( "Now the Top book is ", books[-1])

books.pop()
if not books:
    print("No books left")


#Queue

from collections import deque

bank = deque (["Anis", "Karim", "Bijoy"])
bank.popleft()
print(bank)

if not bank:
    print("No person left")