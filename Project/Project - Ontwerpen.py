from djitellopy import Tello

tello = Tello(); tello.connect()

battery = tello.get_battery()
temperature = tello.get_temperature()
flight_time = tello.get_flight_time()

assert isinstance(battery, int)
assert isinstance(temperature, int)
assert isinstance(flight_time, int)

if battery > 20:
    status = "GO ✅"
else:
    status = "NO-GO ❌"

print("-" * 30)
print("TELLO STATUS REPORT")
print("-" * 30)
print(f"{'Battery':<15}: {battery} %")
print(f"{'Temperature':<15}: {temperature} C")
print(f"{'Flight Time':<15}: {flight_time}")
print(f"{'Status': <15}: {status}")
print("-" * 30)



tello.end()