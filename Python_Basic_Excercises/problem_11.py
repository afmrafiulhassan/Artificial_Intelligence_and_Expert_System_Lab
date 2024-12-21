# Write a Python program to filter positive numbers from a list.

# NOTE: positive numbers start from 1
numbers = [-10, -5, 0, 4, 8, 15]

pos_numbers = []
for x in numbers:
  if x > 0:
    pos_numbers.append(x)

print(pos_numbers)
