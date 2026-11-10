class Speaker:
    def __init__(self):
        self.__volume = 10

    def get_volume(self):
        return self.__volume

    def set_volume(self, value):
        if value < 0 or value > 100:
            return False
        self.__volume = value
        return True



speaker = Speaker()
print(speaker.set_volume(50), (speaker.get_volume()))
print(speaker.set_volume(150), (speaker.get_volume()))
print(speaker.set_volume(-1), (speaker.get_volume()))


speaker.__volume = 100
print(speaker.get_volume())

