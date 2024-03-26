d = {'apple': 3, 'banana': 1, 'cherry': 2}
asc_sorted = dict(sorted(d.items(), key=lambda item: item[1]))
desc_sorted = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print("Sorted by value in ascending order:", asc_sorted)
print("Sorted by value in descending order:", desc_sorted)
