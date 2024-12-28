# Write a Python program to find the total number of even and odd numbers from a given list.

odd_count = 0
even_count = 0

myList = [1,2,3,4,5,6,7,8,9,10]
for x in myList:
  if x%2 == 0:
    even_count += 1
  else:
    odd_count += 1

print("Odd count: ", odd_count, "\nEven count: ", even_count)
