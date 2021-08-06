import random

MAX_NUMBER = 6
MIN_PICK = 1
MAX_PICK = 45


def main():
    picks_number = int(input("How many quick picks do you want? "))
    for num in range(picks_number):
        quick_picks_list = []
        for i in range(MAX_NUMBER):
            numbers = random.randint(MIN_PICK, MAX_PICK)
            while numbers in quick_picks_list:
                numbers = random.randint(MIN_PICK, MAX_PICK)
            quick_picks_list.append(numbers)
        quick_picks_list.sort()
        print(*quick_picks_list)


main()
