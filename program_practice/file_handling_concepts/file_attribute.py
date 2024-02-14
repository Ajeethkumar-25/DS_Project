file = open("demo.txt")
file.close()

is_closed= file.closed # boolean values
print("closed :", is_closed)

file_name = file.name
print("File Name of:", file_name)

file_mode = file.mode
print("File Mode of:", file_mode)
