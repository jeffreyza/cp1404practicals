from datetime import datetime


class GuitarSpecs:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.name} ({self.year}) : ${self.cost:2f}"

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
