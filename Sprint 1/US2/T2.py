battery_percentage = (input("Battery_percentage: "))
percentage_cost_per_minute_to_fly = (input("percentage_cost_per_minute_to_fly: "))

# flight_time = battery / percentage_cost_per_minute_to_fly
# TypeError: unsupported operand type(s) for /: 'str' and 'str'

battery_percentage = int(battery_percentage)
percentage_cost_per_minute_to_fly = float(percentage_cost_per_minute_to_fly)

print(type(battery_percentage))
print(type(percentage_cost_per_minute_to_fly))

flight_time = battery_percentage / percentage_cost_per_minute_to_fly
print("Remaining flight time", flight_time)


