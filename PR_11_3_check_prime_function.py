def is_prime(number):
	if number <= 1:
		return False
	max_divisor = int(number**0.5) + 1
	for i in range(2, max_divisor):
		if number % i == 0:
			return False
	return True

num = 3
print(f"{num} is a prime number" if is_prime(num) else f"{num} is not a prime number")
