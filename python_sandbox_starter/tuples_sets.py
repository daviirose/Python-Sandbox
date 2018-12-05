# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
fruits = ("Apples", "Oranges", "Grapes")
#fruits2 = tuple(("Apples", "Oranges", "Grapes"))

# Single value needs trailing comma
fruits2 = ("Apples",)

print(fruits2, type(fruits2)) # type method tells you its a string or tuple

# Get Value
print(fruits[1]) # Prints out Oranges

# Can't change value 
#fruits[0] = 'pears' # would get error cause tuples are unchangeable

# Delete tuple 
del fruits2 

# Get lengh
print(len(fruits)) 



# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = {"Apples", "Oranges", "Mango"}


# Check if in set 
print('Apples' in fruits_set) # boolean

# Add to set 
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate 
fruits_set.add('Apples')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)
