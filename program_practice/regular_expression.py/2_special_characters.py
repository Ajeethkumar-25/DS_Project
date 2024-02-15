import re

# data ="Python"
# result= re.findall("\APy", data) # \A - whether it checks start with particular data or not
# print(result)

# data ="Python is a high level programming language!"
# result= re.findall(r"\bpro", data) # \b - whether it checks any string start with particular data with "pro"or not
# #  r stands for raw string \b is part of th spl character.
# print(result)

# data ="Python is a high level programming language!"
# result= re.findall("\Bvel", data) # \B - whether it checks any string ends with particular data with "pro"or not

# print(result)

# data ="Python is a high level programming language 132!"
# result= re.findall(r"\d", data) # \B - whether it checks any digits in data
# print(result)
# data ="Python is a high level programming language 132!"
# result= re.findall("\D", data) # \B - whether it checks any Non digit in data
# print(result)

# data ="Python is a high level programming language 132!"
# result= re.findall(r"\s", data) # \s- whether it checks anyspace
# print(result)

# data ="Python is a high level programming language 132!"
# result= re.findall("\S", data) # \S- whether it checks any non space
# print(result)

# data ="Python"
# result= re.findall(r"thon\Z", data) # \Z- whether it checks "thon" ends with the data.
# print(result)

# data ="Python is a high level programming language! 132_"
# result= re.findall("\w", data) # \w- whether it checks the daat contains A-Z, a-z, 0-9,_
# print(result)

data ="Python is a high level programming language! 132_ @#$%^&*()"
result= re.findall("\W", data) # \W- whether it checks the data returns spl char only
print(result)