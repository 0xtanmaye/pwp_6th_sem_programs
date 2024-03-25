li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_items = [item for item in li if item % 2 == 0]
# OR
# even_items = list(filter(lambda x: x % 2 == 0, li))
print("Even items:", even_items)
