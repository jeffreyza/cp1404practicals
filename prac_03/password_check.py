def main():
    password = get_password()
    print_stars(password)


def get_password():
    password = input("Please enter your password: ")
    return password


def print_stars(password):
    print('*' * len(password))


main()
