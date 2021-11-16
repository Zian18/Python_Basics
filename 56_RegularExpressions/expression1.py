import re
pattern = r"color"
text = "My favorite color is Red"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())