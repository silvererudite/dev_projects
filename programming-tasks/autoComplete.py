""" 
Simple autocomplete
given a database and a functionality to search 
autocomplete the words as the user types 
"""

# modelling our database as a simple list

data_list = ["apple", "orange", "banana", "pear", "kiwi", "papaya", "strawberry", "blueberry"]
def autoComplete(word):
  res = []
  for elem in data_list:
    if word in elem:
      res.append(elem)
  return res
print(autoComplete('berry'))
  
