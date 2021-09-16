"""
CP1404/CP5632 Practical
Unreliable Car Test
Jeffrey Timms
"""


from prac_08.unreliable_car import UnreliableCar

my_car = UnreliableCar(name="Lada Vesta 2018", fuel=150, reliability=20)

my_car.drive(50)
print(f"{my_car.name}, attempted to drive 50 miles and managed to drive {my_car.odometer} Mi, there is {my_car.fuel} "
      f"fuel remaining")
