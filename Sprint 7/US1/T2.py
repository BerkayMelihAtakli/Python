class Enemy:
    def __init__(self, x, speed):
        self.x = x
        self.y = 0
        self.speed = speed

    def fall(self):
        self.y += self.speed

class Player:
    def __init__(self, x, speed):
        self.x = x
        self.y = 580
        self.speed = speed


enemy1 = Enemy(100, 3)
enemy2 = Enemy(300, 5)

player = Player(240,6)


enemy1.fall()
enemy1.fall()

player.fall()

print(f"{enemy1.y}")
print(f"{enemy2.y}")

# AttributeError: 'Player' object has no attribute 'fall'

