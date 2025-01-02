# Write a Python program to sort (ascending and descending) a dictionary by value or by key.

my_dict = {'b': 3, 'a': 2, 'c': 1}

# ascending order
dict_key_sorted = dict(sorted(my_dict.items(), key=lambda item: item[0]))
dict_value_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print("Ascending order")
print(dict_key_sorted)
print(dict_value_sorted)

# descending order
dict_key_sorted = dict(sorted(my_dict.items(), reverse=True, key=lambda item: item[0]))
dict_value_sorted = dict(sorted(my_dict.items(), reverse=True, key=lambda item: item[1]))

print("Descending order")
print(dict_key_sorted)
print(dict_value_sorted)
