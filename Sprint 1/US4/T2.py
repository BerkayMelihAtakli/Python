battery = 20

assert isinstance(battery, int), "Error battery should be an integer"

assert battery >= 20, "Error: battery can not be less than 20"

assert battery <= 100, "Error: battery can not exceed 100"

print("All checks passed - ready to fly")

