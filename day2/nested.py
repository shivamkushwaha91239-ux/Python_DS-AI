age = int(input("enter your age: "))
if age>=18:
    license = input("do you have a driving license? (yes/no): ")
    if license.lower() == "yes":
        print("you are eligible for driving")
    else:
        print("you need first to make a driving license")

else:
    print("you are under age ")