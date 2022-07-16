# Process of converting one data type to another

# Implicit: Performed automatically by compiler. int ---> float
# Only on compatible data types. string to int is not compatible

# Explicit: Converting using provided python functions

# int to str
one = 1
my_string = str(one)

print(type(one), type(my_string))

# float to int

two = 2.0
my_int = int(two)
print(type(two), type(my_int))

# int to float

three = 3
my_float = float(three)
print(type(three), type(my_float))

# Other type casting functions

# ord(): integer rep underlying unicode char
# hex(): Converts int to hex
# oct(): Takes integer and return string rep an oct number
# tuple()
# set()
# list()
# dict()
