class Pet:
    def __init__(self, name, kind, age):
        self.name = name
        self.kind = kind
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, kind: {self.kind}, age: {self.age}"

    def __repr__(self):
        return f"Pet: {self.name}, kind: {self.kind}, age: {self.age}"

rex = Pet("Rex", "dog", 3)
mia = Pet("Mia", "cat", 1)
pets = [rex, mia]

print(rex)
print(f"My pet: {rex}")

print(pets)
print(repr(rex))


# - __str__ wordt gebruikt wanneer je een object omzet naar een leesbare tekst voor eindgebruikers.


# - __repr__ wordt gebruikt voor ontwikkelaars en bij debugging
