# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


# Create dict
person = {
    'first_name': 'Davian',
    'last_name': 'Perez-Silva',
    'age': 21
}

print(person, type(person))

# Use constructor
#person2 = dict(first_name='Sarah', last_name='Williams')


# Get value
print(person['first_name']) # Most common way
print(person.get('last_name')) # Get value with get method

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston' # Adding key/value to test

print(person2)

# Remove item
del(person['age']) # Del method
person.pop('phone') # Using pop method

print(person)

# Clear 
person.clear()

# Get Lenght
print(len(person2))

# List of dict
people = [
    {'name': 'David', 'age': 43},
    {'name': 'Barbara', 'age': 40},
]
print(people[1]['name'])

