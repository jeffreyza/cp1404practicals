"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    print("\n========= Limo =========")
    limo = Car(fuel=100)
    limo.add_fuel(20)
    print(f"Fuel in limo: {limo.fuel}")
    distance_driven = limo.drive(115)  # (fuel left = 5, odo = 115km)
    print(f"Odo: {limo.odometer}")
    print(limo)


main()
