import re

# data ="Python is a high level programming language! 132_ @#$%^&*()"
# result= re.findall('[isalrz]', data)   # check if the data contains  i,s,a,l,r,z
# print(result)


# data ="Python is a high level programming language! 132_ @#$%^&*()"
# result= re.findall('[^PBN]', data)   # return characters which are not P,B,N
# print(result)

# data ="Python is a high level programming language! 132_ @#$%^&*()"
# result= re.findall('[c-m]', data)   # return characters which between c and m
# print(result)

# data ="Python is a high level programming language! 132_ @#$%^&*()"
# result= re.findall('[51290]', data)   # returns digits which are 5\1\2\9\0
# print(result)

# data ="78 56"
# result= re.findall('[0-9][8-9]', data)   # returns digits if satisfy the conditions
# print(result)


# data ="Python is a high level programming language! 132"
# result= re.findall('[@]', data)   # returns if data contains @
# print(result)

# data ="Python is a high level programming language! 132"
# result= re.findall('[a-z]{5}', data)   # returns if data contains a-z small letters and 5 charc each
# print(result)
