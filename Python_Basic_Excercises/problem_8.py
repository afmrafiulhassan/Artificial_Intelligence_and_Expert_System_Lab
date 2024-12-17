# Take a character as input and determine whether it is a vowel or not. Therefore, print an appropriate message (vowel/not vowel).

# this program works only for single input value (one alphabet)
in_val = input("Enter an alphaber: ")
if in_val.lower() in ['a', 'e', 'i', 'o', 'u']:
  print("It is a vowel.")
else:
  print("It is a consonant.")
