class Speaker:
    def __init__(self):
        self.__volume = 10

    def get_volume(self):
        return self.__volume

    def set_volume(self, value):
        if value < 0 or value > 100:
            raise ValueError(f"volume must be 0 to 100, got {value}")
        self.__volume = value

speaker = Speaker()

speaker.get_volume()(speaker.set_volume() +)
print(speaker.get_volume)