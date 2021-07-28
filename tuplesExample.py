# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1,2,3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1,"Hello",3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse",[8,4,6],(1,2,3))
print(my_tuple)

# Creating a tuple having one element
my_tuple = ("Hello",)
print(my_tuple)

# Parentheses is optional
my_tuple = "Hello",
print(my_tuple)
print(type(my_tuple))

# Accessing tuple elements using indexing
my_tuple = ('p','e','r','m','i','t')
print(my_tuple[0])
print(my_tuple[5])

# IndexError: list index out of range
#print(my_tuple[6])

# Index must be an integer
#print(my_tuple[2.0])


# nested tuple
my_tuple = ("mouse",[8,4,6],(1,2,3))

# nested index
print(my_tuple[0][3])
print(my_tuple[1][1])

# Negative indexing for accessing tuple elements
n_tuple = ('p','e','r','m','i','t')
print(n_tuple[-1])


# Accessing tuple elements using slicing
m_tuple = ('d','a','f','f','o','d','i','l')
print(m_tuple[1:4])
print(m_tuple[:4])
print(m_tuple[4:])
print(m_tuple[:])


# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del my_tuple[3]

# Can delete an entire tuple
#del m_tuple

# NameError: name 'my_tuple' is not defined
#print(m_tuple)

#Some examples of Python tuple methods:
print(m_tuple.count('f'))
print(m_tuple.index('o'))

print(dir(m_tuple))


