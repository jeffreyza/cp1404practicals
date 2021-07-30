def main():
    for i in range (1, 21 , 2):
        print(i, end=' ')
    print()

    for i in range(0,110, 10):
        print(i, end=' ')
    print()

    for i in range(20, 0, -1):
        print(i, end=' ')
    print()

    stars = int(input("how many stars do you want to print? "))
    for i in range(stars):
        print("*", end=' ')
    print()

    for i in range(1, stars +1):
        print('*' * i)
main()