import re

email =input("Enter the email address:")
result = re.findall(r"^\w+[@][a-z]+[.][a-z]{1,3}$", email)   
print(result)
if result:
    print("The email is Valid")
else:
    print("email is not valid, Check the email again:")