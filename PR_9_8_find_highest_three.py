my_dict = {'a': 100, 'b': 200, 'c': 50, 'd': 300, 'e': 150}
sorted_values = sorted(my_dict.values(), reverse=True)
highest_3_values = sorted_values[:3]
print("Highest 3 values in the dictionary:", highest_3_values)
