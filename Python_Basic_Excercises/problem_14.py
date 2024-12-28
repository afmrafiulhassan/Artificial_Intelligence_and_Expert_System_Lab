# Write a Python program that will sort the numbers of a given list in both ascending and descending order without modifying the original (given) list.

myList = [3,2,1,6,10,4,8,7,9,5]

myAscendingList = sorted(myList)
myDescendingList = sorted(myList, reverse=True)

print("Original List: ", myList)
print("Ascending List: ", myAscendingList)
print("Descending List: ", myDescendingList)
