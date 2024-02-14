file = open("practice.txt", "r")
# data = file.write()
# print(data)

count = 0 
for i in file:
    word = i.split()
    count+= len(word)
print("Count of words:", count)