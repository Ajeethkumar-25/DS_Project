# file= open("qa.txt","w")
# data = file.read()
# print(data)


#1 Swapping the variable:
# input: a=10, b=20
# Output: a=20, b=10


def swap(a,b):
    # temp=a
    # a=b
    # b=temp

    # a, b = b, a
    print(a,b)
swap(10,20)

#2 Program to print the fibonacci series upto n_terms

# Recursive function
def recursive_fibonacci(n):
	if n <= 1:
		return n
	else:
		return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

number = 10
# check if the number of terms is valid
if number <= 0:
	print("Invalid input ! Please input a positive value")
else:
	print("Fibonacci series:")
for i in range(number):
	print(recursive_fibonacci(i))

