class Degree:
	def get_degree(self):
		print("I got a degree")

class Undergraduate(Degree):
	def get_degree(self):
		print("I am an Undergraduate")

class Postgraduate(Degree):
	def get_degree(self):
		print("I am a Postgraduate")

d = Degree()
d.get_degree()

u = Undergraduate()
u.get_degree()

p = Postgraduate()
p.get_degree()
