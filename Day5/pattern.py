for i in range(5):
    for j in range(5):
        print("*", sep=" ", end=" ")

    print()

for i in range(5):
    for j in range(i):
        print("*", end=" ")
    print()