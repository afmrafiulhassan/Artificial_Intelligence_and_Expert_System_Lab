# Define a function that receives a list of values and print all values of the odd indices.

def print_odd_index_values(numbers):
  for ind, val in enumerate(numbers):
    if ind%2 != 0:
      print(val, end=" ")

  print()

print_odd_index_values([1,2,3,4,5,6,7,8,9,10])
