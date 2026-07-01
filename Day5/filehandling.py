# Create and write the file
with open("batch.txt", "w") as f:
    f.write("This is a sample text file.\n")
    f.write("My name is Vansh Dixit.\n")
    
# Read the file
with open("batch.txt", "r") as f:
    content = f.read()
    print(content)
    
# Read line by line
with open("batch.txt", "r") as f:
    for line in f:
        print(line.strip()) # .strip() is used to remove the newline character at the end of each line
        
# Read all lines into a list
with open("batch.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    
# Append to the file
with open("batch.txt", "a") as f:
    f.write("\n")
    f.write("This is an appended line. \n")
    f.write("\n")
    f.write("Appended Again:\nName: Vansh Dixit \nRoll No: 123456 \nAge: 20 \n")

with open("batch.txt", "r") as f:
    content = f.read()
    print(content) 
    