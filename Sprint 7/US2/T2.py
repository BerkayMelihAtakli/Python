class Speaker:
    def __init__(self):
        self.volume = 0

    def change_volume(self, amount):
        self.volume += amount



speaker = Speaker()

speaker.change_volume(5)
print(speaker.volume)
speaker.change_volume(10)
print(speaker.volume)
speaker.change_volume(-3)
print(speaker.volume)

