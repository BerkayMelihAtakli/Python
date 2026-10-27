class Player:

    def __init__(self, name, lives, score):
        self.name = name
        self.lives = lives
        self.score = score

player1 = Player("Berkay",2,60)
player2 = Player("Yaser",2,60)
player3 = Player("Orkun",2,60)
print(player1.name)
print(player2.name)
print(player3.name)


#  orkun = Player(,2,60)
#                    ^
# SyntaxError: invalid sy