lst = [1,2,3,4,5,6,7,8,9,10]

data = list(map(lambda data:"Even" if data%2==0 else "odd", lst))
print(data)