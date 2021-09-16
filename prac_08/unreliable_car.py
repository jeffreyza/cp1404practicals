"""
CP1404/CP5632 Practical
Unreliable_car
Jeffrey Timms
"""


from prac_08.taxi import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_reliability = random.randint(0, 100)
        if self.reliability > random_reliability:
            distance = super().drive(distance)
        else:
            distance = 0

        return distance




