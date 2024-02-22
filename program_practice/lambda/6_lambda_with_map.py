lst = [5,6,2,4,6,7,80,10]

# Using normal way
# def square(data):
#     sq_lst=[]
#     for i in data:
#         sq = i**2
#         sq_lst.append(sq)
#     return sq_lst
# result = square(lst)
# print(result)



# using Map
# def square(data):
#     return data**2
# result = list(map(square,lst))
# print(result)


# using lambda with Map

data =list(map(lambda data:data**2, lst))
print(data)