class Player:
    def __init__(self, name, lives=5, score=0):
        self.name = name
        self.lives = lives
        self.score = score


player1 = Player("Berkay")

player2 = Player("Melih", 3)

player3 = Player("Chris", 10, 250)

print(f"{player1.name} - Levens: {player1.lives}, Score: {player1.score}")
print(f"{player2.name} - Levens: {player2.lives}, Score: {player2.score}")
print(f"{player3.name} - Levens: {player3.lives}, Score: {player3.score}")