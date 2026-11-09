class Enemy:
    def __init__(self, x, speed):
        self.x = x
        self.y = 0
        self.speed = speed

class Player:
    def __init__(self, x, speed):
        self.x = x
        self.y = 580
        self.speed = speed

def fall(thing):
    thing.y += thing.speed

enemy1 = Enemy(100, 3)
player = Player(240, 6)


fall(enemy1)
fall(player)


print(f"{enemy1.y}")
print(f"{player.y}")

# De functie fall() controleert niet bij welk soort object hij hoort.
# Dit geeft geen foutmelding in Python, maar veroorzaakt wel onbedoelde logische fouten.