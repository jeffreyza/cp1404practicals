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




main()
