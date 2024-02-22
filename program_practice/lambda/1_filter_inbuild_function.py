 
# Normal way:
# def even(data):
#     evenlst =[]
#     for i in data:
#         if i%2==0:
#             evenlst.append(i)
#     return evenlst
# result = even(lst)
# print(result)

# using Filter
def even(data):
    return data %2==0
result =list(filter(even,lst))  #logic, Data
print(result)

# result =filter(even,lst) #--> if incase use without list. iteration is not working
# print(result)
# # so we add this method
# for i in lst:
#     print(i)

