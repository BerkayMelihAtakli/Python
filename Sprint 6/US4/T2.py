class Wave:
    def __init__(self):
        self.enemies = []


wave1 = Wave()
wave1.enemies.append("Goblin")
wave1.enemies.append("Orc")
wave1.enemies.append("Dragon")

print(f"Wave1 enemies: {wave1.enemies}")
print(f"Number of Wave1 enemies: {len(wave1.enemies)}")