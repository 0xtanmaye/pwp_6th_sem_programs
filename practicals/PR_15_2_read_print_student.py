class Person:
	def read_info(self):
		self.name = input("Enter name: ")
		self.age = int(input("Enter age: "))

	def print_info(self):
		print("\nName:", self.name)
		print("Age:", self.age)


class Student(Person):
	def read_info(self):
		super().read_info()
		self.grade = input("Enter grade: ")

	def print_info(self):
		super().print_info()
		print("Grade:", self.grade)


student = Student()
student.read_info()
student.print_info()
