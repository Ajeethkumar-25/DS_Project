lst = [5,6,2,4,6,7,80,10]

def even(data):
    evenlst =[]
    for i in data:
        if i%2==0:
            evenlst.append(i)
    return evenlst
result = even(lst)
print(result)
