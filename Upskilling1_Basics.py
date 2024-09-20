f= 5
print(f)
# EVERYTHING IN PYTHON IS AN OBJECT 
x= 5
x += 0.5 
type(x), x
# List - An ordered, mutable collection of items., no need to specify the data type for a list 
lst = [5, 'list', 8.45]
lst
lst[2]
lst[-1] # call the last element 
lst.append('new element appending')
print(lst)
# Adding element at a specific index 
lst.insert(2, 'at index 2')
print(lst)
# removing values from the list 
lst.remove(3)
lst.pop(1)
print(lst)
# ----- to use lst.sort() the values must be of the same type 
len(lst)
# to get specific values in the list 
lst[1:3]
# reverse a string 
s = "hello"
s[::-1]
s[::2] 
# Set - An unordered collection of unique items, with no duplicate values.
#addint value to a set 
set1 = {1,2,3,4,5}
set1.add(6)
set1
# checking if the value is within a set 
8 in set1
set1.remove(2)
set1
# Cimbining sets 
set2 = {6,7,8,9}
set1.union(set2)
# inersection - get common elements 
set1 - set2
# remove matching elements 
set1.intersection(set2)
# 

# Dictionary - like a map, An unordered collection of key-value pairs, where each key is unique.
dict1 = {"name": "Alice", "age": 25}
dict1['age'] # get specific value 
# Adding element to a dictionary 
dict1['key3'] =5655
dict1
# getting just the key or values 
dict1.keys()
dict1.values()
# convert to a list 
x= list(dict1.keys())
print(x)

# Tuples - An ordered, immutable collection of items (cannot be changed after creation).
tup1= (1, 2, 3, "apple")
# cant add anything to it 
m = list(tup1)
m

# CONDITIONS AND IF STATEMENTS 
x = 5 
if x < 10 :
    print("less than 10")
# ************* LOOPS 
count = 1
while count <= 5:
    print(count)
    count += 1
    if count == 3 :
     break

# for 
for i in range(10):
    print(i)

lst = [2,3,6,8,9]
for elem in lst:
    print(elem)
