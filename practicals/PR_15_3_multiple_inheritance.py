class Parent1:
	def method1(self):
		print("Method 1 from Parent1")


class Parent2:
	def method2(self):
		print("Method 2 from Parent2")


class Child(Parent1, Parent2):
	def method3(self):
		print("Method 3 from Child")


child = Child()
child.method1()
child.method2()
child.method3()
