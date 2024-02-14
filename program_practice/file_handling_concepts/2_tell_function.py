# Tell Method - it return to current position of the current file

# file= open("testing.txt", "w")
# position = file.tell()
# print("Before data:", position)
# file.write("Good Morning!!!")
# position = file.tell()
# print("Adding data:", position)

#r - read mode 
file = open("testing.txt", "r")
position = file.tell()
print("Before data:", position)
data = file.read()
print(data)
position = file.tell()
print("Adding data:", position)