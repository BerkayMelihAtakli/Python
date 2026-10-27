class Player:
    lives = 3
    score = 1

player1 = Player()
player2 = Player()

print(player1.lives, "leven  |  ", player1.score, "punten")
print(player2.lives, "leven  |  ", player2.score,  "punten")


print("Hebben beide spelers gelijke punten", player1.score == player2.score)
