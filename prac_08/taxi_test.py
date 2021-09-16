"""
CP1404 Practical
Taxi Test
Jeffrey Timms
"""

from prac_08.taxi import Taxi

prius_1 = Taxi("Prius 1", 100)
prius_1.drive(40)
print(prius_1)
prius_1.start_fare()
prius_1.drive(100)
print(prius_1)
print(f"Fare:${prius_1.get_fare():.2f}")