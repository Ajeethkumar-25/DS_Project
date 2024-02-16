import re

pan =input("Enter the pan number:")
result = re.findall(r"^[A-Z]{5}\d{4}[A-Z]{1}$", pan)   
print(result)

if result:
    print("The pan is Valid")
else:
    print("pan is not valid:")