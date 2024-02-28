# Instance variable
# global variable
# local variable

#############################################################################################################################################
# instance variable - variable defined inside method/constructor with self. as prefix
#                   - scope throughout the class and if you want to access it outside the class then call it via object 
#                   - scope throughout the class and if you want to access it outside the class then
#                     call it via object 
#                   - it is created using self keyword as prefix ex. self.<variable_name>
#                   - different memory is provided for different instance variable
#                   - we can access instance variable via object

############################################################################################################################################
# static/class variable - this variable is defined inside the class but outside the method/
#                         constructor
#                       - scope throughout the class and if you want to access it outside the class then call it via class name 
#                       - class variable can be accessed using both class name and object
#                       - syntax to call it : <object>.<class_variable_name> and <class_name>.<class_variable_name>
#                       - it is used for memory management
#                       - as it shares the same memory
#############################################################################################################################################

# college_name = "Edyoda"                     #global variable
class student:
    college_name = "Edyoda"                     #static/class variable

    def info(self):
        self.name="Ram"                     #instance variable
        self.rno= 78
        address = "bengaluru"               #local variable
    
    def display(self):
        print(f"Name : {self.name} and rno :{self.rno}")

obj = student()
obj.info()
obj.display()
# print("Name: ", obj.name)