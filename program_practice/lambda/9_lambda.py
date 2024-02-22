# lst = [1,2,3,4,5,6,7,8,9,10]
# data =list(map(lambda data:data**2, lst))
# print(data)


# If we have list of n numbers of person and still useris taking input and
# from that we only have to takeout person who's name  starts with 's' then
# ====== practice program ======
# size = int(input("Enter size:"))
# name_lst=[]
# for i in range(size):
#     name = input("Enter  the name:")
#     name_lst.append(name)

# data = dict()
# for i in name_lst:
#     if i[0].lower()=='s':
#         data[i] = 10

# print(name_lst)
# print(data)        



# lst = [45,1,15,57,89,30,46,60,75,90,100]
# # [15,30,45,60,75,90]---op

# data =list(filter(lambda data:data if data%3==0 and data%5==0 else None, lst))
# print(data)


# lst=['apple','banana','orange']
# op==>]['elppa', 'ananab','egnaro']

# data =list(map(lambda data:data[::-1], lst))
# print(data)

# # reverse method() otherway
# data =list(map(lambda data:"".join(reversed(data)), lst))
# print(data)