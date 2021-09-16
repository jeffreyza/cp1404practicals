"""Taxi_simulator
Jeffrey Timms"""
from car import Car
from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def main():
    taxis = [Taxi("Honda Accord", 140), SilverServiceTaxi("Toyota Prius", 200, 3),
             SilverServiceTaxi("Hummer H1", 300, 5)]
    menu = "q)uit, c)hoose taxi, d)drive"
    current_taxi = None
    total_bill = 0
    print("Let's drive!")
    print(menu)
    choice = input("Enter choice: ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxi's Available:")
            display_taxis(taxis)
            current_taxi = taxis[choose_taxi(taxis) - 1]
            print(current_taxi)
        if choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance = int(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_price = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_price:.2f}")
                total_bill += trip_price
            else:
                print("You need to choose a taxi before you can drive")

        print(menu)
        choice = input("Enter choice: ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Select taxi and validate"""
    pick_taxi = int(input("Choose taxi:"))
    if pick_taxi <= 0 or pick_taxi > len(taxis):
        pick_taxi = ""
        print("Invalid Taxi choice")
    return pick_taxi


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i + 1}, {taxi}")


main()