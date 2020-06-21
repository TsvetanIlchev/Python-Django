# STRINGS

my_string = 'abcdefg'
print(my_string)

# Basics
'Hello'
"Hello"

# Indexing
print(my_string[0])
print(my_string[1])

# Slicing
print(my_string[4:])

print(my_string[:3])

print(my_string[2:5])

print(my_string[:])
print(my_string[::2])

# Basic Methods
x = my_string.upper()
print(x)

y = my_string.lower()
print(y)

z = my_string.capitalize()
print(z)

my_sentence = "Hello World"
print(my_sentence.split())

# Print formatting
formatting = "Insert another string here: {}".format("INSERT ME!")
print(formatting)
