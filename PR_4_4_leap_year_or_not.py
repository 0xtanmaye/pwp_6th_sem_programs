year = int(input("Enter an year to check if it is a leap year: "))
if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
	print(year, "is a leap year")
else:
	print(year, "is NOT a leap year")