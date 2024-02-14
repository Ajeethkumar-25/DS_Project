# File Handling
# interacting with files using python is file handling
# types of files?
# textfiles
# binary files
# ####Modes of files
# text file
# r - read mode (bydefault) - it will raise error if file doesn't exist. Itallows us to read the data from file

# w - write (It checks, if file exist. if it exist -> it will overwrite, else it will create a file)
#                It allow to write a file
# a - append -  It creates the file if not exist. 
#               If exist, it doesn't override it, instead it append the data to existing data
#               It allows to write the file
# r+ - same like read mode but it also write the file
# w+ - same like write mode but it also Read the file
# a+ - same like append mode but it also allow to read  the data

# binary File
# rb
# wb
# ab
# rb+
# wb+
# ab+

# write the file
# open(filename,<mode name>)
# file = open("demo.txt", "w")
# file.write("Hello All!, Good Afternoon")
# # whenever opent the file must be close the file
# file.close()


# read the file
file = open("demo.txt",)
data = file.read()
print(data)

# # append the file
# file = open("test.txt", "a")
# file.write("all") 
# # file.write("HEllo") #to append the file
# file.close()

# r+ mode  
# file= open("test.txt", "r+")
# file.write("Edyoda")
# data = file.read()
# print("Data:", data)

# w+ mode
# file= open("testing.txt","w+")
# file.write("Testing")
# data = file.read()
# print(data)

# a+ mode
# file= open("testing.txt", "a+")
# file.write("Hey")
# data = file.read()
# print(data)

# # Q-> why the output gets flashing empty line? 
# # A -> using Seek method()
# file= open("testing.txt", "a+")
# file.write("Hey")
# file.seek(0,0)
# data = file.read()
# print(data)