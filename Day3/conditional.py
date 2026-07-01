age = int(input("Enter your age: "))

if age>=18:
    license = input("Do you have a driving license? (yes/no): ")
    if license.lower() == "yes":
        print("You are eligible to drive.")
    else:
        print("You need a driving license to drive.")   
else:
    print("You are not eligible to drive. You must be at least 18 years old.")
    
    
# Range funciton
for i in range(1,11):
    print(i, end=" ")
print("\n")
    
    
# if elif else
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")