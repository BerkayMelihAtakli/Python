class Wave:
    def __init__(self):
        self.enemies = []



wave1 = Wave()
wave1.enemies.append("Goblin")
wave1.enemies.append("Troll")
wave1.enemies.append("Orc")

print(f"wave1 enemies, {wave1.enemies}")
print(f"numbers of wave1 enemies = {len(wave1.enemies)}")

wave2 = Wave()

print(f"wave2 enemies", wave2.enemies)
print(f"numbers of wave2 enemies =", len(wave2.enemies))
