import re

txt = "HJG 332"

test = re.findall("^[A-Ö]{3} [0-9]{3}$",txt)

print(test)