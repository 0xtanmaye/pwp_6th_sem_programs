def factorial(number):
	if number < 0:
		return None
	result = 1
	for i in range(1, number + 1):
		result *= i
	return result

num = 5
print(f"The factorial of {num} is:", factorial(num))
