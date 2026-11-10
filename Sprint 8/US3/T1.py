class Enemy:
    def __init__(self):
        self.__speed = 3

    def get_speed(self):
        return self.__speed

    def set_speed(self, value):
        if value < 1 or value > 8:
            return False
        self.__speed = value
        return True

enemy = Enemy()

for value in [4, 0, 12, 6]:
    enemy.set_speed(value)

print(enemy.get_speed())



# De waarden 0 en 12 zijn geweigerd, want ze liggen buiten 1 tot 8.
# Het programma meldde dat nergens: er kwam geen foutmelding