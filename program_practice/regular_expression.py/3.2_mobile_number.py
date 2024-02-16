import re

mobile =input("Enter the 10 Digit number:")
result = re.findall(r"^[1-9]{1}[0-9]{9}$", mobile)   #(r"^[1-9]{1}\d{9}$", mobile)  #------>  result starts with 1, next numbers are 0-9
print(result)
if result:
    print("The number is Valid")
else:
    print("Number is not valid, Check the number again:")
