# Python Functions - A function is a block of code which only runs when it is called.
def greet():
    print("Hello from a custom function")
greet()

# ***** Arguments - passed to a parameter (Parameters - inside parentheses) *************
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, 
# just separate them with a comma. The following example has a function with one argument (first_name). 
# When the function is called, we pass along a first name, which is used inside the function to print the full name.
def full_name(first_name):
    print(first_name + " Johnson")
full_name("Alice")
full_name("Bob")
full_name("Charlie")

# Example 2
def combine_names(first_name, last_name):
    print(first_name + " " + last_name)
combine_names("Alice", "Johnson")

# Arbitrary Arguments, *args -- if you don't know how many arguments will be passed into the parameter 
def youngest_child(*children):
    print("The youngest child is " + children[2])
youngest_child("Alice", "Bob", "Charlie")  # The youngest child is Charlie

# Keyword Arguments
def identify_children(child3, child2, child1):
    print("The youngest child is " + child3)
identify_children(child1="Alice", child2="Bob", child3="Charlie")

# Arbitrary Keyword Arguments, **kwargs
"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisks: 
** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments and can access the items accordingly:
"""
def last_name_info(**kid):
    print("His last name is " + kid["lname"])
last_name_info(fname="Bob", lname="Johnson")

# Default Parameter Value
def home_country(country="Canada"):
    print("I am from " + country)
home_country("Mexico")
home_country("India")
home_country()
home_country("Brazil")

# Passing a List as an Argument 
def list_items(items):
    for item in items:
        print(item)
vegetables = ["carrot", "broccoli", "spinach"]
list_items(vegetables)

# Return Values
# To let a function return a value, use the return statement:
def multiply_by_five(x):
    return 5 * x
print(multiply_by_five(3))
print(multiply_by_five(5))
print(multiply_by_five(9))

# The pass Statement
# Function definitions cannot be empty, but if you have a function definition with no content, 
# use the pass statement to avoid getting an error.
def empty_function():
    pass

# Positional-Only Arguments 
# To specify that a function can have only positional arguments, add / after the arguments:
def positional_function(x, /):
    print(x)
positional_function(3)

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments: 
def keyword_function(*, x):
    print(x)
keyword_function(x=3)

# Combine Positional-Only and Keyword-Only
# Any argument before the / is positional-only, and any argument after the *, is keyword-only.
def combine_all(a, b, /, *, c, d):
    print(a + b + c + d)
combine_all(5, 6, c=7, d=8)

# ******* Recursion -- defined function calling itself 
def recursive_sum(k):
    if(k > 0):
        result = k + recursive_sum(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
recursive_sum(6)
