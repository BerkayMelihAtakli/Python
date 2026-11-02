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
        self.color = (255, 255, 255)


class Enemy:
    def __init__(self, x, y, speed, alive=True):
        self.x = x
        self.y = y
        self.speed = speed
        self.alive = alive

        self.width = 40
        self.height = 40
        self.color = (255, 80, 80)


player = Player(x=220, y=550, speed=15)

enemies = []
for _ in range(10):
    x_pos = random.randint(-100, 100)
    y_pos = random.randint(-100, 100)
    speed = random.randint(2, 6)
    enemies.append(Enemy(x=x_pos, y=y_pos, speed=speed))

enemies[1].alive = False

living_enemies = 0
for enemy in enemies:
    if enemy.alive:
        living_enemies += 1


print(f"Living enemies: {living_enemies}, from the {len(enemies)} enemies")
print(f"Status enemies 1 = {enemies[1].alive}")

run_game(player, enemies)

