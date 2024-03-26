list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_items = [item for item in list1 if item in list2]
# OR
# common_items = list(set(list1).intersection(list2))
# common_items = list(set(list1) & set(list2))
print("Common items:", common_items)
