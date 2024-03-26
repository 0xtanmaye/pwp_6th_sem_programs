try:
	dividend = int(input("Enter dividend: "))
	divisor = int(input("Enter divisor: "))
	if divisor == 0:
		raise ZeroDivisionError("Error: Division by zero")

	result = dividend / divisor
	print("Result:", result)

except ZeroDivisionError as e:
	print(e)
