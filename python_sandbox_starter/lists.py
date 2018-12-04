# A List is a collection which is ordered and changeable. 
# Allows duplicate members.

# Create list

numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
#numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get lenght
print(len(fruits))

# Append to list. To add
fruits.append('Mangos')

print(fruits)

# Remove from list

fruits.remove('Grapes')

print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')

print(fruits)

# Change value
fruits[0] = 'Quenepas'

print(fruits)

# Remove with pop
fruits.pop(2)

print(fruits)

# Reverse list
fruits.reverse()

print(fruits)

# Sort list in alphabetical order
fruits.sort()

print(fruits)

# Reverse sort

fruits.sort(reverse=True)

print(fruits)

