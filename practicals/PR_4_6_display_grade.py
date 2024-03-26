total = 0
for i in range(5):
	total = total + float(input(f"Enter the marks of subject {i+1}: "))
per = (total / 500) * 100
if (per >= 85):
	print("A Grade")
elif (per >= 70):
	print("B Grade")
elif (per >= 55):
	print("C Grade")
elif (per >= 35):
	print("D Grade")
else:
	print("Fail")