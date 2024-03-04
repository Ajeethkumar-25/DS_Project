class grandpa:
    def field(self):
        print("Field")

class dad(grandpa):                               
    def flat(self):
        print("flat")
    def car(self):
        print("car")

class son(dad):                       
    def mobile(self):
        print("Mobile")
    def bike(self):
        print("Bike")
        

obj = son()
obj.bike()
obj.mobile()
obj.flat()
obj.car()
obj.field()

