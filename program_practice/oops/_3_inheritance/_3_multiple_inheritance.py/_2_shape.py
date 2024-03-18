# QA is 
# area of circle
        # circle_area(radius)
        # display()
# area of Square
# area of Rectangle
# area of triangle

# area

class area_circle:
	def c_area(self):
		rad = int(input("Enter radius of the circle: "))
		self.area = 3.16*rad*rad
	def c_display(self):
		print("Area of the circle:", self.area)

class area_square:
	def s_area(self):
		side = int(input("Enter length of side of the square: "))		
		self.area = side*side
	def s_display(self):
		print("Area of the square:", self.area)

class area_rectangle:
	def s_area(self):
		len = int(input("Enter length of the rectangle: "))
		wide = int(input("Enter width of the rectangle: "))
		self.area = len*wide
	def r_display(self):
		print("Area of the rectangle:", self.area)

class area_triangle:
	def t_area(self):
		height = int(input("Enter height of the triangle: "))
		base = int(input("Enter length of base of the triangle: "))
		self.area = 1/2*(base*height)
	def t_display(self):
		print("Area of the triangle:", self.area)

class Area(area_circle,area_square,area_rectangle,area_triangle):
	def ques(self):
		shape = input("What do you want to find the Area for? ").lower()
		return shape


obj = Area()
shape = obj.ques()
if 	shape == "circle":
	obj.c_area()
	obj.c_display()
elif shape == "square":
	obj.s_area()
	obj.s_display()
elif shape == "rectangle":
	obj.r_area()
	obj.r_display()
elif shape == "triangle":
	obj.t_area()
	obj.t_display()

else: 
	print("Invalid Input, try again!")