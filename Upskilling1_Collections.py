value = 5
print(value)
# EVERYTHING IN PYTHON IS AN OBJECT 
num = 5
num += 0.5 
type(num), num

# ***************************LISTS**********************************************
# List - An ordered, changeable collection of items, that allows duplicates, and can store different data types.
# no need to specify the data type for a list 
# From Python's perspective, lists are defined as objects with the data type 'list':
# *************************************************************************
""" Methods 
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

# -1 refers to the last item, -2 refers to the second last item etc.
my_list = [5, 'example', 8.45]
my_list
my_list[2]
my_list[-1] # call the last element 
my_list.append('new item added')
print(my_list)

# 1. A list can contain different data types:
mixed_list = ["xyz", 34, True, 40, "female"]
print(mixed_list)

# 2. Adding element at a specific index 
my_list.insert(2, 'at index 2')
print(my_list)

# 3.  Removing values from the list 
my_list.remove(3)  # This will raise an error as 3 is not in the list
my_list.pop(1)
print(my_list)

# 4. ----- to use my_list.sort() the values must be of the same type 
len(my_list)

# 5. To get specific values in the list 
my_list[1:3]

# 6. Reverse a string SLICING 
text = "hello"
text[::-1] # reverses the string 
text[::2] # this slice selects every second character from the string starting with 0, 2, 4 etc. so result is ' hlo '

# 7. What is the datatype of a list: 
fruits_list = ["apple", "banana", "cherry"]
print(type(fruits_list)) # it is a list 

# 8. ** Range of Indices: 
fruit_basket = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruit_basket[2:5]) # specifying which range to print by setting the index 

# 9. Check if the item exists: 
fruit_basket = ["apple", "banana", "cherry"]
if "apple" in fruit_basket:
  print("Yes, 'apple' is in the fruit basket")

# 10. *** CHANGE THE ITEMS OF THE LIST 
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket[1] = "blackcurrant"
print(fruit_basket)

# 11. Change the range of items 
fruit_basket = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruit_basket[1:3] = ["blackcurrant", "watermelon"]
print(fruit_basket)

# 12. Change the second value by replacing it with two new values (one additional will be added):
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket[1:2] = ["blackcurrant", "watermelon"]
print(fruit_basket)

# 13. Change the second and third values by replacing them with one value:
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket[1:3] = ["watermelon"]
print(fruit_basket)

# 14. INSERT method 
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket.insert(2, "watermelon")
print(fruit_basket)

# 15. Append method 
# to add items to the list 
fruit_basket = ["apple", "banana", "cherry"]
fruit_basket.append("orange")
print(fruit_basket)

# 16. Extend method 
# used to append elements from another list to the current list, use the extend() method.
fruit_basket = ["apple", "banana", "cherry"]
tropical_fruits = ["mango", "pineapple", "papaya"]
fruit_basket.extend(tropical_fruits)
print(fruit_basket)

# 17. Extend can be used to add any collections: 
fruit_basket = ["apple", "banana", "cherry"]
fruit_tuple = ("kiwi", "orange")
fruit_basket.extend(fruit_tuple)
print(fruit_basket)

# 18*** LOOP THROUGH A LIST 

# ~~using a FOR loop ~~; In Python, when you use a for loop to iterate over a list, 
# The loop automatically takes care of assigning each element of the list to the variable specified in the loop.
# Create a list containing three elements
fruit_basket = ["apple", "banana", "cherry"]
for an item in fruit_basket: # Iterate over each element in the list
    print(item) # Print the current element

# 19~~Using a WHILE loop ~~ 
fruit_basket = ["apple", "banana", "cherry"]
index = 0  # Initialize the index
while index < len(fruit_basket):  # Continue looping while the index is less than the length of the list
    print(fruit_basket[index])  # Access and print the element at index
    index = index + 1  # Increment index to move to the next index

# 20*** Looping Using List Comprehension - shortest syntax 
# new_list = [expression for item in iterable if condition == True]
fruit_basket = ["apple", "banana", "cherry"]
[print(item) for item in fruit_basket]

# 21. Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [item.upper() for item in fruits]
print(new_list)

# 22. Set all values in the new list to 'hello':
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = ['hello' for item in fruits if 'k' in item]
print(new_list)

# 23. Substitute one word for another 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [item if item != "banana" else "orange" for item in fruits]
print(new_list)

# 24. SORT in descending order 
sorted_fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
sorted_fruits.sort(reverse=True)
print(sorted_fruits)

# 25. **** DEFINING FUNCTIONS: and using them in sort and other predefined functions: 
# You can also customize your own function by using the keyword argument key = function.

def length_function(s): # Define a function that returns the length of a string
    return len(s)

fruits = ["banana", "apple", "kiwi", "grapefruit", "cherry"] # Create a list of fruit names
fruits.sort(reverse=True, key=length_function) # Sort the list using the defined function as the key
print(fruits) # Print the sorted list

# 26. Sort is CASE SENSITIVE: By default, the sort() method is case sensitive, resulting in all capital 
# letters being sorted before lowercase letters:
# use str.lower key function 
# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:
case_fruits = ["banana", "Orange", "Kiwi", "cherry"]
case_fruits.sort(key=str.lower)
print(case_fruits)

# 27. Use the copy() method to copy the list 
fruit_basket = ["apple", "banana", "cherry"]
copied_list = fruit_basket.copy() # list(fruit_basket) method would also work or the following fruit_basket[:]
print(copied_list)

# 28. Join Lists 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
combined_list = list1 + list2
print(combined_list)

# 29. Appending items of the list from a to b 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for item in list2:
  list1.append(item)
print(list1)

# **************************SET**********************************************
# Set - An unordered collection of unique items, with no duplicate values.
# *************************************************************************
# Adding value to a set 
unique_set = {1, 2, 3, 4, 5}
unique_set.add(6)
unique_set
# Checking if the value is within a set 
8 in unique_set
unique_set.remove(2)
unique_set
# Combining sets 
set2 = {6, 7, 8, 9}
unique_set.union(set2)
# Intersection - get common elements 
unique_set - set2
# Remove matching elements 
unique_set.intersection(set2)

# ******************************DICTIONARY*******************************************
# Dictionary - like a map, An ordered collection of key-value pairs, where each key is unique and changeable.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# *************************************************************************
# The data type of the dictionary is dict  
# 1. Getting the value 
profile_dict = {"name": "Alice", "age": 25}
profile_dict['age']  # Get specific value 
# or use method .get()
name_value = profile_dict.get("name")
print(name_value)

# 2. Adding elements to a dictionary 
profile_dict['key3'] = 5655
profile_dict['age'] = 21
profile_dict

# 3. Getting just the keys or values 
profile_dict.keys()
profile_dict.values()

# 4. Convert to a list 
keys_list = list(profile_dict.keys())
print(keys_list)

# 5. Get items() - The items() method will return each item in a dictionary, as tuples in a list.
items_view = profile_dict.items()
items_view
profile_dict

for key, value in profile_dict.items():
    print(f"Key: {key}, Value: {value}")

# 6. Check if the key exists 
car_info_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in car_info_dict:
    print("Yes, 'model' is one of the keys in the car_info_dict dictionary")

# 7. Update Dictionary
car_info_dict.update({"year": 2020})

# 8. Removing Items 
# The pop() method removes the item with the specified key name:
vehicle_info_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
vehicle_info_dict.pop("model")
print(vehicle_info_dict)

# The del keyword removes the item with the specified key name:
vehicle_info_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del vehicle_info_dict["model"]
print(vehicle_info_dict)

# del can delete the dictionary completely 
vehicle_info_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del vehicle_info_dict
# print(vehicle_info_dict)  # this will cause an error because "vehicle_info_dict" no longer exists.

# The clear() method empties the dictionary:
vehicle_info_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
vehicle_info_dict.clear()
print(vehicle_info_dict)

# 9. Loop Dictionaries 
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
#a. For loop: Print all key names in the dictionary, one by one:
vehicle_info_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in vehicle_info_dict:
    print(x)

#b. Print all values in the dictionary, one by one:
vehicle_info_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in vehicle_info_dict.values():
    print(x)

#c. You can use the keys() method to return the keys of a dictionary:
for x in vehicle_info_dict.keys():
    print(x)

#d. Loop through both keys and values, by using the items() method:
for x, y in vehicle_info_dict.items():
    print(x, y)

# 10. COPY dictionary 
#a. Make a copy of a dictionary with the copy() method:
vehicle_info_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
my_vehicle_dict = vehicle_info_dict.copy()
print(my_vehicle_dict)

# b. Make a copy of a dictionary with the dict() function:
vehicle_info_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
my_vehicle_dict = dict(vehicle_info_dict)
print(my_vehicle_dict)

# 11. Nested Dictionaries - a dictionary within a dictionary 
#a. Create a dictionary that contain three dictionaries:
my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

#b. Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
kid1 = {
    "name": "Emil",
    "year": 2004
}
kid2 = {
    "name": "Tobias",
    "year": 2007
}
kid3 = {
    "name": "Linus",
    "year": 2011
}
my_family = {
    "child1": kid1,
    "child2": kid2,
    "child3": kid3
}

#c. Access items in nested dictionaries. To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
# Print the name of child 2:
print(my_family["child2"]["name"])

# d. Loop through nested dictionary using items()
for x, obj in my_family.items():
    print(x)  # Print the key (e.g., 'child1', 'child2', 'child3')
    for y, value in obj.items():  # Use obj.items() to get key-value pairs
        print(y + ':', value)  # Print the key and value


# *************************************************************************
# Tuples - An ordered, immutable collection of items (cannot be changed after creation).
# *************************************************************************
tuple_example = (1, 2, 3, "apple")
# Can't add anything to it 
mutable_list = list(tuple_example)
mutable_list

# CONDITIONS AND IF STATEMENTS 
value_check = 5 
if value_check < 10:
    print("less than 10")

# ************* LOOPS 
counter = 1
while counter <= 5:
    print(counter)
    counter += 1
    if counter == 3:
     break

# for 
for index in range(10):
    print(index)

numbers_list = [2, 3, 6, 8, 9]
for element in numbers_list:
    print(element)
