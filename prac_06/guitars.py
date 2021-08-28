from prac_06.guitar_specs import GuitarSpecs


def main():
    print("My Guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add_guitars = GuitarSpecs(name, year, cost)
        guitars.append(add_guitars)
        print(f"{add_guitars} added.")
        name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage = ""
        if guitar.is_vintage():
            vintage = "(Vintage)"
        print(f"Guitar {i}: {guitar.name}, {guitar.year},worth: ${guitar.cost:.2f} {vintage}")


main()
