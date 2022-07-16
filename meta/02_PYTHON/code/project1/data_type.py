# Python Data types
# Numeric, Sequence, Dictionary, Boolean, Set

# Numeric: int, float, complex numbers

# Using type() to identify data type

x = 10
y = 5.0
z = 10 + 10j

print(type(x), type(y), type(z))

# Sequence: Strings, List, Tuples (Immutable)

name = 'Jame'
aList = [1, 'hello', 5.4, "A"]
example_tuple = (1, 'hello', 5.4, "A")

print(type(name), type(aList), type(example_tuple))

# Dictionary (Key: Value) Value accessed by key
ed = {'a': 22, 'b': 44.4}
print(ed['a'])

# Boolean
print(type(True))
print(type(False))

# Set (Uses dictionary type brackets)

example_set = {1, 'hello', 5.4, "A"}
print(type(example_set))
