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


# Tijdens elke Player(...) aanroep verwijst self steeds naar het specifieke object dat op dat moment wordt aangemaakt