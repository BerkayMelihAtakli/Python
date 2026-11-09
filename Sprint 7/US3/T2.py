class Player:
    def __init__(self):
        self.health = 0

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

player = Player()

player.health = 3

if player.is_alive():
    print("Playing")
else:
    print("Game Over")

player.health = 0

if player.is_alive():
    print("Playing")
else:
    print("Game Over")

player.health = 3

h = player.get_health()

print(h - 1)




