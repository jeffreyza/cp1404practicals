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

    shady_authenticator()


def shady_authenticator():
    """Authenticates user based on username given."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    get_name = input("What is your username? ")
    if get_name in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()