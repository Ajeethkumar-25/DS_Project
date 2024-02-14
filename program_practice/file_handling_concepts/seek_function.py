# seek - it allows the modify the position of the cursor
# seek(offset, from_what)
# offset - no of position to shift
# from_what - point of reference(start)

# from_what - only accept 3 values
# 0 - begining the value (bydefault value is 0)
# 1 - current  position ofn the file
# 2 - end of the file


# file = open(" demo.txt", "w")
# cur_pos = file.tell()
# print("Current Position before: ",cur_pos) 
# file.seek(4,0)
# cur_pos = file.tell()
# print("Current Position After: ",cur_pos) 
# file.write("Hey")
# cur_pos = file.tell()
# print("After having data: ",cur_pos)


# a+ Mode

file = open("new.txt", "a+")
file.write("Hey")
data=file.read()
print(data)