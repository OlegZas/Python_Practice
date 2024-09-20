print("Hello, World!");
print(50);
if 5 > 2: 
    print ('Oleg');

""""
another comment
"""
# *********** VARIABLES *************************
x = 5 #no command for declaring variables 
y = 10
print (x+y);
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
# type () - used to get the datatype of the variable 
x = 5 
y = "John"
print(type(x))
print(type(y))
""" NAMING CONVENTIONS 
Variable names can be short (e.g., x, y) or descriptive (e.g., age, carname).
Must start with a letter or underscore (_).
Cannot start with a number.
Can contain only letters, numbers, and underscores (A-Z, 0-9, _).
Case-sensitive (e.g., age, Age, AGE are different).
Cannot be a Python keyword.
"""
a, b, c = "mike", "jeff", "oscar"
print(a)
print(b)
print(c)
d = e = "cat"
print(d,e)
# upacking - collecitons/lists can be extracted into variables 
names = ["jorge", 'susan', 'kate']
l,m,n = names
print(n,"name", l,m)
# Global Variables - defined outside of the function and can be used in the funcitons 
x = "OZ"
def myfunc():
    print('OZ Python', x)
myfunc ()
#
x = "cat" # this is a global variable 
def myfunc():
  global y 
  y = "horse"
  x = "dog"
  print("Animal is " + x)
myfunc()
print("Animal is " + x + y)
# ********************* DATATYPES ************************
"""
Example	Data Type	
x = str("Good Morning") -----	str	
x = int(42)	----- int	
x = float(15.8)	----- float	
x = complex(3j)	----- complex	
x = list(("cat", "dog", "mouse"))	----- list	
x = tuple(("cat", "dog", "mouse"))	----- tuple	
x = range(10)	----- range	
x = dict(name="Alice", age=25)	----- dict	
x = set(("cat", "dog", "mouse"))	----- set	
x = frozenset(("cat", "dog", "mouse"))	----- frozenset	
x = bool(7)	----- bool	
x = bytes(8)	----- bytes	
x = bytearray(8)	----- bytearray	
x = memoryview(bytes(8))	----- memoryview
"""
# 9/19/2024 
# Float - contains decimals and can have scientific e
m = 54.45
print(type(m))
# Complex - numbers are written with a j as imaginary part 
u =1j
print(u)
# ****type conversion ****
k = int(m)
p=1
o = str(m)
print(k, float(p), type(o))
# for random numbers use 
# import random 
print(random.randrange(1,689))
# ****************************
# ************************************ STRING ***************
# ************ INDEX OF ELEMENTS OF THE STRING : 
e = 'Oleg'
print(e[3])
# *********** LOOPING THROUGH A STRING: 
for x in 'olegario':
    print(x)
# ********* STIRNG LENGTH
a = 'Olegor'
print(len(a))
# ***** check if a character or a string is present in a stirng:
print('O' in a) # return boolean TRUE/False 
if "O" in a :
    print("yes, O is in", a)
# **** Check if NOT
print("O" not in a) # TRUE / FALSE 
if "M" not in a : 
    print(a)
# SLICING - return a range of characters from x to y from a string
print(a[2:4])
# SLICING from the begging 
print (a[:3])
# SLICE from x to the end 
print (a[1:])
# SCLIDE FROM END OF THE STRING -- negative indexing 
print (a[-3:-1]) # Olegor = go .. indexing starts from 1 
# ****** MODIFYING STRING 
print(a.upper())
print(a.lower())
# Remove whitespace (space before or after the string)
# strip ()
a = ' Oleg, Best ' 
print(a.strip())
# Replace() - replaces a string with antoher 
print(a.replace('Oleg', 'Jack'))
# split() - returns a list wehre the text between the separator is the list of items 
print(a.split(','))
#Concatenation
b = " won"
c = a+b
print(a + b )
print(c)
# ** Combining STRINGS and NUMBERS 
# cant simply do STRING + INT .. will result in error 
age =  22
g = f"""oleg 
{age:.2f}  
best"""
print(g)# :.2f is a modifier reformatting the vlaue to 2 decimals 
# **** ESCAPE CHARACTERS 
# inserting illegal characters for ex: double quote witin a string 
a = "Oleg is \"Olegor\" of the world"
print(a) 
"""
Code	Result	
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
"""
