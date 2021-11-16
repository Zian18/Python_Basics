class Phone:
   
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")

class Samsung(Phone):
    # def call(self):
    #     print("You can call")
    
    # def message(self):
    #     print("You can message")
    
    def photo(self):
        print("You can take photo")

# p = Phone()
# p.message()
# p.call()

s = Samsung()
s.message()
s.call()
s.photo()
print (issubclass(Samsung,Phone))  #phone is superclass or parentclass