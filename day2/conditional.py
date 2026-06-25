# wap to check if student passes or fails based on marks
marks = int(input("Enter the marks of student: "))
if marks >= 40:
    print("Student has passed")
else:
    print("Student has failed")


#wap to check is eligible for driving license or not
age = int(input("Enter the age of person: "))
if age >= 18:
    license = input("Does the person have a driving license? (yes/no): ")
    if license.lower() == "yes":
        print("Person is eligible for driving license")
    else:
        print("Person is not eligible for driving license")
else:
    print("Person is not eligible for driving license")


    #wap to check if a number is even or odd
number = int(input("Enter a number:"))
if number %2 ==0:
    print("the number is even")
else:
    print("the number is odd")


 # Range function
for i in range(1,11):
     print(i)

#checking number is negative or positive
num = int(input("Enter a number: "))
if num>0:
    print("the number is positive")
elif num<0:
    print("the number is negative")
else:
    print("the number is zero")