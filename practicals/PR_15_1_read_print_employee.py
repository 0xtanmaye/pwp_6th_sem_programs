class Employee:
	def read_info(self):
		self.name = input("Enter employee name: ")
		self.department = input("Enter department: ")
		self.salary = float(input("Enter salary: "))

	def print_info(self):
		print("Employee Information:")
		print("Name:", self.name)
		print("Department:", self.department)
		print("Salary:", self.salary)


emp = Employee()
emp.read_info()
emp.print_info()
