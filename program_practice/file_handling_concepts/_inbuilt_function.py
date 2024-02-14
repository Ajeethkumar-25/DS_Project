file = open("result.txt", "w")

# data = file.read()
# print(data)



# data = file.read(2) # read 2 character
# print(data)



# data = file.readline() # read the first line
# print(data)

# data = file.readlines() # read the first line
# print(data)

# for i in data:
#     print(i, end="")
# del data[2]
# print(data)


lst = ["test\n","text\n","write\n","read\n","book\n", "ajeeth\n"]

file.writelines(lst)