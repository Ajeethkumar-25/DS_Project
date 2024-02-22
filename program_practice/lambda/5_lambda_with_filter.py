#  Using lambda and filter

#  cannot define it in another function as a argument


lst = [5,6,2,4,6,7,80,10]

data =list(filter(lambda data:data%2==0, lst))
print(data)
