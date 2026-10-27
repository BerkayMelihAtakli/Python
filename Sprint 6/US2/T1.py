class Player:

    def __init__(self, name, lives, score):
        self.name = name
        self.lives = lives
        self.score = score

berkay = Player("Berkay",2,60)
yaser = Player("Yaser",2,60)
orkun = Player("Orkun",2,60)
print(berkay.name)
print(yaser.name)
print(orkun.name)


#  orkun = Player(,2,60)
#                    ^
# SyntaxError: invalid syntax