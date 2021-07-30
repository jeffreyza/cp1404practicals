def main():
    names_file = "names.txt"
    out_file = open(names_file, 'w')
    user_name = input("What is your name? ")
    print(user_name, file=out_file)
    out_file.close()


    data = open('names.txt', "r")
    read_name = data.read().strip()
    data.close()
    print("Your name is", read_name)

    numbers = open("numbers.txt", "r")
    read_numbers1 = int(numbers.readline())
    read_numbers2 = int(numbers.readline())
    numbers.close()
    print(read_numbers1 + read_numbers2)

    numb_total = 0
    all_numbers = open("numbers.txt", "r")
    for numb in all_numbers:
        number = int(numb)
        numb_total += number
    all_numbers.close()
    print(numb_total)


main()