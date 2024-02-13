# 1st way
# import a # import <module_name>


# # <module_name>.<function_name>
# a.greet()
# print(a.name)

# 2nd way
# alias
# import a as demo 
# demo.greet()
# print(demo.name)


# 3rd way
# # from<module_name>import<function_name, variable, class_name>
# from a import greet, name

# greet()
# print(name)

# 4th way
# from<module_name>import * (all)
from a import *

greet()
print(name)

print("Name in b is:", __name__)