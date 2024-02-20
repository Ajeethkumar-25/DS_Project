import re 

data = "Python is a programming language"
result = re.search("is",data)              #if there is match it shows, match objects, else it shows none
print(result)

data = "Python is a programming language"
result = re.search("Ajeeth",data)              #if there is match it shows, match objects, else it shows none
print(result)

if result:
    print("Successfull, it shows match object")
else:
    print("itshows None")