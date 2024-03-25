li = [10, 30, 5, 50, 40]
# OR
# smallest_num = min(li)
smallest_num = li[0]
for num in li:
	if num < smallest_num:
		smallest_num = num
print("Smallest number in the list:", smallest_num)
