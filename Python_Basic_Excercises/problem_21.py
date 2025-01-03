# Define a search function that receives a dictionary and a target value. Therefore, check if the target value exists in the dictionary values and return the corresponding key of the dictionary where the target value is found.

def search_dictionary(myDict, target):
  for key, val in myDict.items():
    if val == target:
      return key

  return None

targetIndex = search_dictionary({'a': 1, 'b': 2, 'd': 4, 'c': 3}, 4)

if targetIndex != None:
  print("Value found in index: ", targetIndex)
else:
  print("Target value not found.")
