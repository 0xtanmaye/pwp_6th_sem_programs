num1, num2 = 0, 1
fibonacci_series = []

limit = int(input("Enter the limit for Fibonacci series: "))

while num1 < limit:
	fibonacci_series.append(num1)
	num1, num2 = num2, num1 + num2

print(f"Fibonacci series up to {limit}: {fibonacci_series}")
