# when you have a multiple set of values but return with single value.
# filter, map funtions are return multiple values, reduce doesnt return multiple value.
# reduce function doesnt have direct access, import package (**)
from functools import reduce
lst = [5,6,1,4,2,3,8,7,9]

# Using normalway
# def list_sum(data):
#     sum=0
#     for i in data:
#         sum+=i
#     return sum
# result = list_sum(lst)
# print(result)



# using map
def list_sum(data, data1):
    return data+data1
result = reduce(list_sum, lst)  #------reduce doesnt return multiple value. So only list() is not required
print(result)