import os

# #deletes the file:
# os.remove("trail.txt")
# # checks if given file addressed or not
# is_exist = os.path.exists("practice.txt")
# print(is_exist)

# # deletes the folder to use this:::Folder needs to be empty
# os.rmdir("D:\\DS Projects\\DS_practice\\program_practice\\file_handling_concepts\\test")
# #

# # creating a file :
# file= open("D:\\DS Projects\\DS_practice\\program_practice\\filehandling\\test1.txt", "w")


# x- mode : It create the file, if the file already exist then it will throw an error
file_name = "ajeeth.txt"
if os.path.exists("file_name")==False:
    file =open("file_name","x")
    print("File got created")
else:
    print("File already exist")


