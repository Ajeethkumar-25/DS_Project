lst = [67,5,15,6,4,7,53,2,89,41]

def square(data):
    sq_lst=[]
    for i in data:
        sq = i**2
        sq_lst.append(sq)
    return sq_lst
result = square(lst)
print(result)

# def square(data):
#     return data**2
# result = list(map(square,lst))
# print(result)