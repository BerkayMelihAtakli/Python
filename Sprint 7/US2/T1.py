class Speaker:
    def __init__(self):
        self.volume = 0

    def volume_up(self):
        self.volume += 1

    def volume_down(self):
        self.volume -= 1

    def volume_down_3(self):
        self.volume -= 3

    def volume_up_5(self):
        self.volume += 5

    def volume_up_10(self):
        self.volume += 10

speaker = Speaker()

speaker.volume_up()
speaker.volume_up()
speaker.volume_up()

print(f"Before - volume = {speaker.volume}")

speaker.volume_down_3()
speaker.volume_up_5()
speaker.volume_up_10()

print(f"After - volume = {speaker.volume}")




