class Pet:
    def __init__(self, name, kind, age):
        self.name = name
        self.kind = kind
        self.age = age

    def __repr__(self):
        return f"Pet('{self.name}', '{self.kind}', {self.age})"

rex = Pet("Rex", "dog", 3)
other_rex = Pet("Rex", "dog", 3)
older_rex = Pet("Rex", "dog", 4)
pets = [Pet("Rex", "dog", 3), Pet("Mia", "cat", 1), Pet("Tom", "cat", 7)]