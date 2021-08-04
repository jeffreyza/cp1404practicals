def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    numbers[0] = "ten"
    numbers[-1] = 1
    print(numbers[2:])
    if 9 in numbers:
        print("This number is an element of numbers")
    else:
        print("This number is not an element of numbers")


if __name__ == "__main__":
    main()
