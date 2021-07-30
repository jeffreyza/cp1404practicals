"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("enter score: "))
    check_score(score)
    print(check_score(score))
    random_score = random.randint(0, 100)
    print("Your random score is", random_score, "and it is a", check_score(random_score))


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid score!"
    elif score >= 90:
        return "Excellent score"
    elif score >= 50:
        return "Passable score"
    else:
        return "Bad Score"


main()
