player_x = 220
score = 0
enemies = []
runnning = True


def add_score(points):
            global score
            score += points

add_score(10)
print(f"score = {score}")

# # Globale variabelen van het spel
# player_x = 220    # Houdt de horizontale positie (X-coördinaat) van de speler op het scherm bij
# score = 0         # Houdt de huidige score van de speler bij
# enemies = []      # Een lijst die alle actieve vijanden in het spel opslaat
# running = True    # Een boolean die aangeeft of de game-loop nog actief is of moet stoppen