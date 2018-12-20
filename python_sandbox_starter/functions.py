# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print(f'Hello {name}')

sayHello("Davian") 

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total # Return will let you associate your parameter with variables

#print(getSum(3, 4))
num = getSum(3, 4)
print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Very similar to JS arrow functions

getSum = lambda num1 , num2 : num1 + num2

print(getSum(10, 3))

def hello(name, lastname): # define the function # passing through parameters
    fullname = name + lastname # give paramters a variable
    return fullname # return it so it can associate with variable

myfullname = hello('Davian ', 'Perez-Slva') # Call it and give it a variable
print(myfullname) # print the new variable that holds the function
