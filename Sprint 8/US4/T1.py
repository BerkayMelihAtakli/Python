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

speaker.set_volume(speaker.get_volume() + 10)
print(speaker.get_volume())

speaker.volume = 80
print(speaker.get_volume())
print(speaker.volume)



# Er zijn nu twee losse waarden (attributen) op het object:
# - __volume (intern opgeslagen als _Speaker__volume) met waarde 20. Dit is het echte volume.
# - volume met waarde 80.