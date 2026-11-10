class Enemy:
    def __init__(self):
        self.__speed = 3

    def get_speed(self):
        return self.__speed

    def set_speed(self, value):
        if value < 1 or value > 8:
            raise ValueError(f"Value must be between 1 and 8, got {value}")
        self.__speed = value


enemy = Enemy()

for value in [4, 0, 12, 6]:
    try:
        enemy.set_speed(value)
        print("speed set to", value)
    except ValueError as error:
        print("refused", error)

print(enemy.get_speed())


# Zonder try/except zou het programma stoppen bij de eerste ongeldige
# waarde (0) met een ValueError, en de rest van de lus zou niet meer
# draaien. Een fout kun je dus niet negeren.
# Het voordeel ten opzichte van return False: de fout valt altijd op en
# bevat een boodschap die zegt wat er misging, terwijl een False stil
# genegeerd kan worden.








