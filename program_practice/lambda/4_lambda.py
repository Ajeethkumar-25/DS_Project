# Lambda
# What is lambda?==>interniew qa
# It is an anonymous function
# it is a function withou an Name
# it can have any number of arguments but can only have one expression(Condition).
#  It is use to create one liner function
# it doesnt supportm multiliner function
# we dont need return statement in lambda

# Diff b/w lambda and function?==>interniew qa

# Functions
# needs name
#  it can have any number of expression in lambda
#  required return statement
#  cannot define it in another function as a argument

# def fun(a,b):
#     return a+b
# data = fun(7,8)
# print(data)

# #convert to lambda


# syntax is lambda <arguments, arguments1> : <expressions>
data = lambda a,b:a+b
print(data(7,8))