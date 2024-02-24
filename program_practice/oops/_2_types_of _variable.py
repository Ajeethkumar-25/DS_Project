# Instance variable
# global variable
# local variable

college_name = "Edyoda"                     #global variable
class student:
    def info(self):
        self.name="Ram"                     #instance variable
        self.rno= 78
        address = "bengaluru"               #local variable
    
    def display(self):
        print(f"Name : {self.name} and rno :{self.rno} and College name:{college_name}")

obj = student()
obj.info()
obj.display()
print("Name: ", obj.name)