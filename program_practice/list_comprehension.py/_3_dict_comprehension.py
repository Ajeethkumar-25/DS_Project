# dict comprehension --> is use to create a new dict from another type of data


# str = "Python"
# dict ={i.upper():i.lower()for i in str}   #--->{key:values}
# print(dict)

# key = [1,2,3,4]
# value = ["ram", "sita", "ajeeth", "vijay"]
# # Zip() -used to combine the values in one dictonary
# dict1 = {i:j for i,j in zip(key,value)}
# print(dict1)


lst = [2,3,4,5,6]
# op-- >{2:[2,4,6,8,10,...],3:[3,6,9,12,15,....],..........}
dict_comp = {i:[i*2 for i in range(1,11)] for i in lst}
print(dict_comp)