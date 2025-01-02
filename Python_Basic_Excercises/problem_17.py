# Write a Python program to print a specified list after removing the elements from some specific positions such as removing 0th, 4th and 5th elements from a list of length 6.

numbers = [-10, -5, 0, 4, 8, 15]
new_numbers = []
for ind, val in enumerate(numbers):
  if ind not in [0,4,5]:
    new_numbers.append(val)

print("After removing: ", new_numbers)
