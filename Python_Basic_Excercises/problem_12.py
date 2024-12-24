# Write a Python function (user defined/not built-in) to find the maximum and minimum numbers from a sequence of numbers.

from re import M
def my_max(numbers):
  mx = -100
  for x in numbers:
    if x > mx:
      mx = x

  return mx

def my_min(numbers):
  mn = 100
  for x in numbers:
    if x < mn:
      mn = x
  return mn

m = my_max([-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50])
n = my_min([-50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50])
print("Max: ", m, "\nMin: ", n)
