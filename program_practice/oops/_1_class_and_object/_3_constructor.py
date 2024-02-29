# Constructor
# It is a special kind of function
# It is defined using __init__()
# You need not have call if explain it gets called automatically when an object is created
# It is used to create an object
# It is use to initialize instance variable
# constructor has same name as class name
# constructor  bydefault gives you an object, so it doesn't acceptreturn statement


# NOTE:      its not recommended to write logical code inside constructor

# Types of constructor:
# Default construtor: when you dont create  an constructor of your  class, then compileer provides an default condtructor
# Zero constructor: Constructor without parameter
# parameterized constructor : Constructor with parameter


class constructor:
    def __init__(self, name, rno):
        self.name= name
        self.rno = rno
    
    def display(self):
        print(f"Name: {self.name} \nand rno: {self.rno}")

    
obj = constructor("Ajeeth", 23)                     #creating object
obj.display()
obj1 = constructor("Sivani", 24)
obj1.display() 
obj2 = constructor("Ramya", 25)
obj2.display()   
# obj.__init__() -- Not required but it also works 


# Anything we have end with () bracket means its a function
