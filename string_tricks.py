# convert string to list of strings
str1 = "Python pool for python knowledge"
list1 = list(str1.split(" ")) 
print(list1) 

# convert string to list of characters in Python
str1 = "Python pool for python knowledge"
list1 = list(str1)
print(list1) 

# Convert List of Strings to List of Lists using map in Python
str1 = "Python pool for python knowledge"
str1=str1.split()
list1=list(map(list,str1))
print(list1)

# Convert string consisting of Integers to List of integers in Python:
str1="9 8 7 6 5 4 3 2 1"
list1=list(str1.split())
list2=list(map(int,list1))
print(list2)

# String to list in Python using custom separator:
str1 = "Python-pool-for-python-knowledge"
list1 = list(str1.split("-")) 
print(list1) 

# Parsing string to list using JSON:
import json
json_str = '{"str": ["Python", "pool", "for", "python", "knowledge"]}'
json_obj = json.loads(json_str)
list1 = json_obj["str"]
print(list1)

# Parsing string to list using ast:
import ast 
 
str1 = "['Python', 'pool','for','python', 'knowledge']"
print (type(str1)) 
print(str1)
list1 = ast.literal_eval(str1) 
print (type(list1)) 
print (list1)
























