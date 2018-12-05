# Strings in python are surrounded by either single or double quotation marks. 

name = 'Davian'
age = 21

# Concatenate
#print('Hello, my name is ' + name + ' and I am ' + str(age))


# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)

print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count how many 'h' are inside the s variable
sub = 'h'
print(s.count(sub))

# Starts with, returns boolean
print(s.startswith('hello'))

# Ends with, returns boolean
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric, returns boolean
print(s.isalnum())

# Is all alphabetic, returns boolean
print(s.isalpha())

# Is all numeric, returns boolean
print(s.isnumeric())