li = [10, 30, 80, 50, 40]
# OR
# largest_num = max(li)
largest_num = li[0]
for num in li:
	if num > largest_num:
		largest_num = num
print("Largest number in the list:", largest_num)
