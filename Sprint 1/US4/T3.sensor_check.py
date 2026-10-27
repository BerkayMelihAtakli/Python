# Importeer de Tello-klasse uit de djitellopy bibliotheek om de drone te besturen
from djitellopy import Tello

# Initialiseer een nieuw Tello-drone object om acties mee uit te voeren
tello = Tello()

# Maak verbinding met de Tello-drone via Wi-Fi
tello.connect()

# Vraag het huidige batterijpercentage op als sensorwaarde van de drone
battery = tello.get_battery()

# Controleer door middel van een assert of het batterijpercentage groter is dan 20
assert battery > 20, "The battery is too low to proceed (20% or less)."

# Sluit de verbinding met de Tello-drone netjes af en beëindig het programma
tello.end()