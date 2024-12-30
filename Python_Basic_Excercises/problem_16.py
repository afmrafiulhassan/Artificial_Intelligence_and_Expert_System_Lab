# Take a line of text (words separated by spaces) as input and find two words that have the highest and the lowest length.

text_line = input("Enter string: ")
words = text_line.split(" ")

max_word = min_word = words[0]
max_len = -100
min_len = 100
for w in words:
  current_len = len(w)
  if current_len > max_len:
    max_len = current_len
    max_word = w
  if current_len < min_len:
    min_len = current_len
    min_word = w

print("Hghest length word: ", max_word, "\nLowest length word: ", min_word)
