from importlib.resources import open_text


class Pet:
    def __init__(self, name, kind, age):
        self.name = name
        self.kind = kind
        self.age = age

    def __repr__(self):
        return f"Pet('{self.name}', '{self.kind}', {self.age})"


rex = Pet("Rex", "dog", 3)
other_rex = Pet("Rex", "dog", 3)


print(rex == other_rex)
print(rex is other_rex)

pets = [rex]

print(other_rex in pets)
print(pets.count(other_rex))


unsorted_pets = [Pet("Rex", "dog", 3), Pet("Mia", "cat", 1)]

try:
    print(sorted(unsorted_pets))
except TypeError as error:
    print(error)


# == kijkt standaard naar de plek in het geheugen, niet naar de inhoud.
# in gebruikt achter de schermen == en vindt daardoor niets.
# sorted() werkt niet omdat de class Pet geen regel heeft die bepaalt welk object "kleiner" (<) is.

