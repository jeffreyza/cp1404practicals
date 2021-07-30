"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
This will occur if the input is not a valid integer.
2. When will a ZeroDivisionError occur?
This occurs if the input has a value of 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
yes I implemented a while loop that asks again if the user enters 0 as the denominator
and will exit the loop and print finished if the user enters a denom above 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("You cannot divide by 0, try another denominator")
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")