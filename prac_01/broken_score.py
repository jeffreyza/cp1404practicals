"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def main():
    score = float(input("enter score: "))
    if score < 0 or score > 100:
        print("Invalid score!")
    elif score >= 90:
        print("Excellent score")
    elif score >= 50:
        print("Passable score")
    else:
        print("Bad Score")
main()
