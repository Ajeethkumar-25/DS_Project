# Multiple Inheritance - When we have a multiple parent class and single inheritance

class dad:
    def car(self):
        print("Car")
    def bangalow(self):
        print ("bangalow1")

class mom:
    def jewellery(self):
        print("jewellery")
    def bangalow(self):
        print ("bangalow")

class son(dad, mom):
    
    def mobile(self):
        print("Mobile")

    def bangalow(self):
        print("Son Bangalow")

obj = son()

obj.mobile()
obj.car()
obj.bangalow()
obj.jewellery()

# O/P:
# Mobile
# Car
# bangalow1   ----> Whichever you class you calling  first, it shows the method on that class.
# jewellery

# O/P2:
# Mobile
# Car
# Son Bangalow ----->fifo concept in the class son
# jewellery


print(son.mro())  #MRO - Method resolution order
print(son.__mro__)