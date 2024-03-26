class Area:
	def print_area(self, length=None, breadth=None):
		if length is not None and breadth is not None:
			print("Area of rectangle:", length * breadth)
		elif length is not None:
			print("Area of square:", length ** 2)
		else:
			print("Invalid arguments provided")

area = Area()
area.print_area(4, 6)
area.print_area(5)
