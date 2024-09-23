# Python Lambda
# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.
# syntax: lambda arguments : expression
temperature_conversion = lambda temp: temp + 32  # temp is like a parameter
print(temperature_conversion(2))  # Output: 34

# VS the standard: 
def add_fahrenheit(value):
    return value + 32

print(add_fahrenheit(2))  # Output: 34

# Lambda can take any number of arguments 
multiply = lambda a, b: a * b
print(multiply(5, 6))  # Output: 30

sum_values = lambda a, b, c: a + b + c
print(sum_values(5, 6, 2))  # Output: 13

# Lambda inside of the function 
def multiplier(factor):
    return lambda number: number * factor

double_function = multiplier(2)
print(double_function(11))  # Output: 22

triple_function = multiplier(3)
print(double_function(11))  # Output: 22
print(triple_function(11))   # Output: 33
