class Pet:
    def __init__(self, name, kind, age):
        self.name = name
        self.kind = kind
        self.age = age

rex = Pet(f"Rex", f"dog", 3)
mia = Pet(f"Mia", f"cat", 1)
yaser = Pet(f"Yaser", f"monkey", 21)
pets = [rex, mia, yaser]


print(rex)
print(pets)


print(f"Name: {rex.name}, kind: {rex.kind}, age: {rex.age}")
print(f"Name: {mia.name}, kind: {mia.kind}, age: {mia.age}")
print(f"Name: {yaser.name}, kind: {yaser.kind}, age: {yaser.age}")

# Bij stap 3 moet je steeds opnieuw handmatig dezelfde f-string met alle attributen uitschrijven voor elk nieuw object dat je wilt printen.