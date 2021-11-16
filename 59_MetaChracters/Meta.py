import re
import re

pattern = r"a*"

if re.match(pattern,"aaacoloubar"):
    print("matched")
else:
    print("unmatched")