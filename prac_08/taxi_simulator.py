from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi
from car import Car

def main():
    taxis = [Taxi("Honda Accord", 140), SilverServiceTaxi("Toyota Prius", 200, 3), SilverServiceTaxi("Hummer H1", 300, 5)]
    current_taxi = None
    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)drive")
    choice = input("Enter choice: ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxi's Available:")
            display_taxis()
        if choice == "d":


        else:
            print("Invalid menu choice")
        choice = input("Enter choice: ").lower()


def display_taxis(taxis)
    for i, taxi in enumerate(taxis):
        print(f"{i}, {taxi}")