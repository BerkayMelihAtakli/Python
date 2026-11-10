class Thermostat:
    def __init__(self):
        self.__target = 20

    def show(self):
        print(self.__target)

t = Thermostat()