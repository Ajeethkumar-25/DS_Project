import re
pin =input("Enter the 6 Digit Pincode:")

pattern = re.compile("^[1-9]{1}[0-9]{5}$")
print(pattern)
result = re.search(pattern, pin)    
print(result)


if result:
    print("Th pin is correct")
else:
    print("The pin is wrong")
