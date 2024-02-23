#  class
# syntax
# class <class_name>:
#     body
# class - It is the blueprint(planning)
# Object - it is the instance of the class
#method - every function defined inside the class must have '(self)' keyword as first "parameter"

# self - it's a keyword.
#        it represents current class object.



# Methods == functions which are created inside the class are known as method!
# 
class Building:                                 #class
    def door(self, no_of_doors):                             #method
        print(f"Building has total {no_of_doors} Doors!")
    
    def windows(self):
        self.door(65)
        print("Building has 80 Doors!")

building_obj = Building()                           #object creation

building_obj.door(40)
building_obj.windows()                              #calling class via object

