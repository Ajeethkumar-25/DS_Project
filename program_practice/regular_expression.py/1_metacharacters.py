import re


data ="Hello"
# result =re.findall("[a-z]",data) #It checks the letter should be in smalls

# print(result)

# result =re.findall("[A-Z]",data)#It checks the letter should be in chapital

# print(result)

# result =re.findall("[A-z]",data)#It checks the letter should be in capital& smalls

# print(result)


# data ="Hello123"
# result =re.findall("[A-Za-z]",data)

# print(result)


# data ="Hello123"
# result =re.findall("\d",data)#It checks the data contains digits

# print(result)

# data ="Hello123"
# result =re.findall("\s",data)#It checks the data contains spaces

# print(result)

# data ="Hello 123"
# result =re.findall("H...o",data)#It checks the data contains word which started in H ends with O

# print(result)

# data ="Hello raj"
# result =re.findall("^He",data)#It checks the data contains word which started in captial(^)H or not. 

# print(result)

# data ="Hellllooo raj"
# result =re.findall("aj$",data)#It checks the data contains word which ends with "aj" or not. 

# print(result)


# data ="Hellllooo raj"
# result =re.findall("He.+o",data)#It checks the data contains word which starts with "He" and ends with o. inbetween it must 1 or more characters

# print(result)


# data ="Helo raj"
# result =re.findall("He.?o",data)#It checks the data contains word which starts with "He" and ends with o. inbetween it may have 0 or 1 characters

# print(result)

# data ="Hello raj"
# result =re.findall("He.*o",data)#It checks the data contains word which starts with "He" and ends with o. inbetween it may have 0 or more characters

# print(result)

# data ="Helllo raj"
# result =re.findall("He.{3}o",data)#It checks the data contains word which starts with "He" and ends with o. inbetween it may have 0 or 1 characters

# print(result)

# data ="Helllo raj, how are you?"
# result =re.findall("Raj|you|are",data)#It checks the data contains word is present in data.

# print(result)