
from sympy import python


name = "Alice"
age = 18
height = 5.6
in_student = True

print(name, age, height, in_student)

# type conversion

x = "100"
y = int(x)  
z = float(x)
s = str(y)

print("x", x, "type:", type(x))
print("y", y, "type:", type(y))
print("z", z, "type:", type(z))
print("s", s, "type:", type(s))

# Strings

text = "Python Programming"

print(text.upper())
print(text.lower())
print(text.replace("Python", "Ajgar"))
print(text)
print(text.split())
print(type(text.split()))
print(len(text))


# Python Collections

fruits = ["apple", "banana", "cherry", "date"] # list
cord = (1, 2, 3, 4) # tuple
student = {"name": "Alice", "age": 18, "height": 5.6} # dictionary
uniqueNames = {"Alice", "Bob", "Charlie"} # set

print(fruits)
print(cord)
print(student)
print(uniqueNames)

# bitwise operator
a = 6
b = 10

print("a & b:", a & b)  # AND: gives 1 if both bits are 1, else gives 0
print("a | b:", a | b)  # OR: gives 1 if any of the bits is 1, else gives 0
print("a ^ b:", a ^ b)  # XOR: gives 1 if bits are different, else gives 0

# symbol of XOR is ^ and it is called exclusive OR. symbol is Caret

print("~a:", ~a) # NOT: gives the complement of the number (~ is Tilde)
print("a << 1:", a << 1)  # Left Shift: shifts bits to the left (<< >> is Guilletments)
print("a >> 1:", a >> 1)  # Right Shift: shifts bits to the right
print(a << b) 
