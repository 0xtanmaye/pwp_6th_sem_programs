set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = set1.intersection(set2)
print("Intersection:", intersection)

union = set1.union(set2)
print("Union:", union)

difference = set1 - set2
print("Set difference:", difference)

symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric difference:", symmetric_difference)

set1.clear()
print("Set1 after clearing:", set1)
