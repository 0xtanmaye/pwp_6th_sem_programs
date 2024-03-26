class IncorrectPasswordError(Exception):
	pass


def check_password(pwd):
	correct_pwd = "password123"
	if pwd != correct_pwd:
		raise IncorrectPasswordError("Error: Incorrect password")


try:
	pwd = input("Enter password: ")
	check_password(pwd)
	print("Password is correct")

except IncorrectPasswordError as e:
	print(e)
