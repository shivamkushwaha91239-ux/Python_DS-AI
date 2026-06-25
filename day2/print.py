#method 1
print("Hello world")

#method 2
message = "Hello world"
print(message)

#method 3
text1 = "Hello"
text2 = "world"
print(text1 + " " + text2)

#method 4
message = "Hello world"
print(f"{message}")

#method 5
import sys
sys.stdout.write("Hello world\n")

#method 6
def greet():
    return "Hello world"

# data types
a= [2, 3, 4, 5]
print(type(a))

print("current array:", a)

#list and array operations
#append method
a.append(6)
print("append element 6 at last:", a)

# append at fix index 
a.insert(2, 7)
print("append at index 2 :", a)

#slicing
marks = [10, 20, 30, 40, 50]
marks1 = [10, 20, 30, 40, 50]
marks1[2:4] = [35, 45]
print("marks before slicing:", marks)
print("marks after slicing:", marks1)

