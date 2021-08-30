
class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self) -> str:
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, first appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
