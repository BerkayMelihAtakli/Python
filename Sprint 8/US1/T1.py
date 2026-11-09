class Player:
    def __init__(self):
        self.health = 5

p = Player()

p.health = -50
print(p.health)
p.health = 999
print(p.health)
p.health = "dood"
print(p.health)

p.helth = 5
print(vars(p))

# levens: -50 is lager dan 0, 999 is hoger dan 5 en "dood" is geen getal.