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
