d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined_dict = {}
for key in d1.keys() | d2.keys(): # combine (union) the keys of d1 and d2
	combined_dict[key] = d1.get(key, 0) + d2.get(key, 0)

print("Combined dictionary:", combined_dict)
