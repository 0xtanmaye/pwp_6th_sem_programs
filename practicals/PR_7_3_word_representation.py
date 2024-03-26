number = 29610
digit_words = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
word_representation = ' '.join(digit_words[int(digit)] for digit in str(number))
print(f"{number} => {word_representation}")
