class Game:
    def __init__(self, width, height):
        self.width = 50
        self.height = 50



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



