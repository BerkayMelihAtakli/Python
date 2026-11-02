class Player:
    def __init__(self, x, y, speed, alive=True):
        self.x = x
        self.y = y
        self.speed = speed
        self.alive = alive

        self.width = 40
        self.height = 40
        self.color = "blue"



    def print_info(self):
        print(f"---- Player1 ----  x = {Player1.x}, y = {Player1.y}, speed = {Player1.speed}, alive = {Player1.alive}, width = {Player1.width}, height = {Player1.height}, color = {Player1.color}")

Player1 = Player(10, 20, 30, True)
Player1.print_info()

Player1.alive = False
Player1.print_info()




