"""
CP1404/CP5632 Practical
Jeffrey Timms
Count occurrences of words in a string
"""


def main():
    emails = {}
    email = input("Enter your email: ")
    while email != "":
        name = name_extract(email)
        check = input(f"Is your name {name}? (Y/N)").lower()
        if check != "y" and check != "":
            name = (input("Name:"))
        emails[email] = name
        email = input("Email: ")
    for email, name in emails.items():
        print(f"{name} ({email})")


def name_extract(email):
    email_split = email.split('@')[0]
    domain_split = email_split.split('.')
    name = " ".join(domain_split)
    return name


if __name__ == '__main__':
    main()
