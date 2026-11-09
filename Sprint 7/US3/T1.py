class Player:
    def __init__(self):
        self.health = 3

    def show_health(self):
        print(self.health)

player = Player()

player.show_health()


answer = player.show_health()

print(answer)


# In een commentaar staat dat print alleen iets laat zien en dat je code er niets mee kan.

# if player.show_health() > 0:
#     IndentationError: expected
#     an
#     indented
#     block
#     after
#     'if'
#     statement
#     on
#     line
#     16