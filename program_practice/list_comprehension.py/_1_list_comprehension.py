# List comprehension - it is use for creating a new list from another list


# for i in list:
#     if condition:
#         body


# syntax
# [body for i in lst if condition]


nums = [1,2,3,4,5,6,7,8,9,10]
# using normal way
# new_lst = []
# for i in nums:
#     if i%2==0:
#         new_lst.append(i)

# print(new_lst) 

# Using List comprehension
# data = [i for i in nums if i%2==0]
# print(data)



# QA
# str = "PYTHON"
# op==> ['P','Y','T','H','O','N']

# data = [i for i in str]
# print(data)

# lst =['apple', 'mango', 'aeroplane', 'ac', 'laptop', 'mobile','diary']
# # starts with a and length greater than 4

# data = [i for i in lst if i[0]=='a' and len(i)>4]
# print(data)


lst = [1,2,3,4,5,6,7,8,9,10,11,12]
# op ==> return the odd position not odd values.

data =[i for i in lst if lst.index(i)%2!=0]
print(data)
# various way
data =[i for i in lst[1:len(lst):2]]
print(data)

# various way
data =[lst[i] for i in range(len(lst))if i%2!=0]
print(data)