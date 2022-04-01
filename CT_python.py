# First Program
print("Hello World!")
# New Components
'Programming'+'Rocks'+'!'
2+2
'''Variables'''
# Make program easier to understand
# They have names that aim to memory values
# Operator (=) associates a variable with a value 
# Variables cannot be called as reserved words.
my_int = 1      # Integer
my_float = 1.0  # Float
my_bool = False # Boolean
my_none = None  # NoneType
type(my_int)
type(my_float)
type(my_bool)
type(my_none)
'''It's important to assing correct names to variables.'''

'''Assigning new values to variables'''
# We change the pointer
my_var = 'Hello World!'
print(my_var)
id(my_var)      #Place where is located
my_var = 3
print(my_var)
id(my_var)      #Place where is located

'''Strings'''
#len()      String's length
#index()    Index 
#slice()    [start, stop, step]
my_str = "Hello World!"
len(my_str)
my_str[0]
my_str[0:5:1]

print(f'I love to say {my_str}') # Amusing way to write