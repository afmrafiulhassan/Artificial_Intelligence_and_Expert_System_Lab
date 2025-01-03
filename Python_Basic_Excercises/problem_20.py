# Write a Python program to merge two dictionaries. [may use: copy(), update()].

dict1 = {'a': 1, 'b': 2}
dict2 = {'d': 4, 'c': 3}

dict1.update(dict2)
print(dict1)

# use the code below if you don't want to modify the original dictionary
# dict3 = { **dict1, **dict2}
# print(dict1)
# print(dict2)
# print(dict3)
