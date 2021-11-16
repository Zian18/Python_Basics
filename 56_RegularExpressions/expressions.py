import re
import re

pattern = r"Color"

if re.match(pattern,"Color is a color, I love red colour"):
    print("MAtch")
else:
    print("Not Matched")

if re.search(pattern,"Color is a color, I love red colour"):
    print("MAtch")
else:
    print("Not Matched")

print(re.findall((pattern,"Color is a color, I love red colour")))