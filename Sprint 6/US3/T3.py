import random
from game_engine import run_game

class Player:
    def __init__(self, x, y, speed, alive=True):
        self.x = x
        self.y = y
        self.speed = speed
        self.alive = alive

        self.width = 40
        self.height = 40
        self.color = "white"


class Enemy:
    def __init__(self, x, y, speed, alive=True):
        self.x = x
        self.y = y
        self.speed = speed
        self.alive = alive

        self.width = 40
        self.height = 40
        self.color = (255, 50, 50)

player = Player(220, 550, 5)

enemies = []

for _ in range(10):
    x_position = random.randint(0, 450)
    y_position = random.randint(0, 450)
    speed = random.randint(0, 10)
    enemies.append(Enemy(x=x_position, y=y_position, speed=speed))

enemies[2].alive = False
enemies[5].alive = False


living_enemies = 0
for enemy in enemies:
    if enemy.alive:
        living_enemies += 1


print(f"Living enemies: {living_enemies} from the {len(enemies)} enemies")
print(f"Status enemie 2: {enemies[2].alive}")
print(f"Status enemie 3: {enemies[3].alive}")

run_game(player, enemies)







