tup = (1, 2, 3, 2, 4, 5, 2, 6, 7, 8, 8)
repeated_items = []
for item in tup:
	if tup.count(item) > 1 and item not in repeated_items:
		repeated_items.append(item)
# OR
# repeated_items = set(item for item in tup if tup.count(item) > 1)
print("Repeated items:", repeated_items)
