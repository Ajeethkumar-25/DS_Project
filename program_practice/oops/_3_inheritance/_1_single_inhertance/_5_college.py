class College:
    def __init__(self, college_name, college_address):
        self.college_name = college_name
        self.college_address = college_address

    def display_college(self):
        print (f"College Name: {self.college_name} \nCollege Address : {self.college_address}")

class Student(College):
    def __init__(self, student_name, student_address, college_name, college_address):
        super().__init__(college_name, college_address)
        self.student_name = student_name
        self.student_address = student_address

    def display_student(self):
        print (f"Student Name: {self.student_name} \nStudent Address : {self.student_address}")

student = Student("Ajeeth","Tamil Nadu", "Kongu", "Erode")
student.display_student()
student.display_college()


