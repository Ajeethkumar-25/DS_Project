from functools import reduce
lst = [5,6,1,4,2,3,8,7,9]

data = reduce(lambda data, data1:data+data1, lst)
print(data)