# Conditional if statement
a = 10
if (a > 5):
    print("a is greater than 5")

#LIST/ARRAY OPERATIONS
a = [1, 2, 3, 4, 5]
print(type(a))

print("curr array:", a)

# append element 6 
a.append(6)
print("append 6 in array:", a)

# append element 7 at index 1
a.insert(1, 7)
print("append 7 at index 1 in array:", a)


# slicing in lists
print("sliced array:", a[1:4])
a[2:4] = [8, 9]
print("after slicing and replacing:", a)