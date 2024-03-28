num = int(input("Enter a number: "))
reverse_num = 0
while num:
	digit = num % 10
	reverse_num = reverse_num * 10 + digit
	num //= 10

print("Reversed number:", reverse_num)
