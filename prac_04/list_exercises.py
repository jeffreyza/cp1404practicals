def main():
    numbers=[]
    print("Please enter 5 numbers")
    for i in range(1,6):
        numbers_request = int(input(f"Number {i}: "))
        numbers.append(numbers_request)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print(f"The average number is", sum(numbers) / len(numbers))


main()