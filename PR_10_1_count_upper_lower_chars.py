def count_case_letters(s):
	uc = sum(1 for c in s if c.isupper())
	lc = sum(1 for c in s if c.islower())
	return uc, lc

input_string = "Hello World"
upper_count, lower_count = count_case_letters(input_string)
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
