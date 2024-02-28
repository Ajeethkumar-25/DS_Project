class college:

    college_name = "Edyoda"           # class / static variable - Hence there are two ways of calling  class object
                                      # either we using class name or object both will work

    def __init__(self,sname,sno,saddress):
        self.sname = sname
        self.sno = sno
        self.saddress = saddress

    def display(self):
        print("Student college : ",college.college_name)
        print("Student Name : ",self.sname)
        print("Student Roll No : ",self.sno)
        print("Student Address : ",self.saddress)
        
college.college_name = "coder"

print(college.college_name)
college_obj1 = college("Ajeeth", 89, "Chennai")
print(college_obj1.college_name)
college_obj1.display()

print(college.college_name)
college_obj2 = college("sivani", 26, "Mumbai")
print(college_obj2.college_name)
college_obj2.display()

print(college.college_name)
college_obj3 = college("vinod", 83, "pune")
print(college_obj3.college_name)
college_obj3.display()
# obj.college()
# obj.display
