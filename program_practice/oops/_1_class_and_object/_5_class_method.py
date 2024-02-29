# class method - are used to specifically deal with static/class variable

class college:

    college_name = "Edyoda"                             # class / static variable

    def __init__(self,sname,sno,saddress):              # constructor
        self.sname = sname
        self.sno = sno
        self.saddress = saddress

    def display(self):                                  # instance method
        print("Student college : ",college.college_name)
        print("Student Name : ",self.sname)
        print("Student Roll No : ",self.sno)
        print("Student Address : ",self.saddress)


college_obj1 = college("Aryan",89,"Mumbai")
print(college_obj1.college_name)
college_obj1.display()