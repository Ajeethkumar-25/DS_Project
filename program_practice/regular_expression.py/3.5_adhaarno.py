import re

adhaar =input("Enter the adhaar number:")
result = re.findall(r"^[1-9]{1}\d{3}\s[0-9]{4}\s\d{4}$", adhaar)   
print(result)

if result:
    print("The Adhaar is Valid")
else:
    print("Adhaar is not valid:")