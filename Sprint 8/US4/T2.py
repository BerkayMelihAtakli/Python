class Speaker:
    def __init__(self):
        self.volume = 10

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        if value < 0 or value > 100:
            raise ValueError(f"volume must be 0 to 100, got {value}")
        self.__volume = value

speaker = Speaker()

speaker.volume = 80
print(speaker.volume)
speaker.volume += 10
print(speaker.volume)

try:
    speaker.volume = 150
except ValueError as error:
    print(f"Refused : error")

print(speaker.volume)