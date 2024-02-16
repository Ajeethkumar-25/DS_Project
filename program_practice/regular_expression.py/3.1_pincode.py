import re
pin =input("Enter the 6 Digit Pincode:")
result = re.findall(r"[1-9]{1}[0-9]{5}$", pin)    #------>  result starts with 1, next numbers are 0-9
print(result)


if result:
    print("Th pin is correct")
else:
    print("The pin is wrong")

