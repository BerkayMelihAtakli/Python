class Player:
    lives = 3
    score = 1

player1 = Player()
player2 = Player()
player3 = Player()

player1.name = "Berkay"
player2.name = "Anouk"
player3.name = "Chris"

player1.score += 10

player2.lives -= 1


print(f"{player1.name}, {player1.lives} leven {player1.score} punten")
print(f"{player2.name}, {player2.lives} leven {player2.score} punten")
print(f"{player3.name}, {player3.lives} leven {player3.score} punten")

