class Printer:
	def print_int_char(self, num, char):
		print(f"Integer: {num}, Character: {char}")

	def print_char_int(self, char, num):
		print(f"Character: {char}, Integer: {num}")

printer = Printer()
printer.print_int_char(10, 'A')
printer.print_char_int('B', 20)
