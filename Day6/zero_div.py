try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    #attemppt division
    result = numerator / denominator
    print(f"The result of the division is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero. Please enter a non-zero denominator.")

except ValueError:
    print("Error: Invalid input. Please enter valid integers for numerator and denominator.")

finally:
    print("Execution completed.")          