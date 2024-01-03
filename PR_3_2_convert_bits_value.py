bits_value = int(input("Enter the number of bits: "))
mb_value = bits_value / 8000000 #OR: bits_value * 0.000000125
gb_value = bits_value /8000000000 #OR: bits_value * 0.000000000125
tb_value = bits_value / 8000000000000 #OR: bits_value * 0.000000000000125
print(f"{bits_value} bits = {mb_value} MB")
print(f"{bits_value} bits = {gb_value} GB")
print(f"{bits_value} bits = {tb_value} TB")
