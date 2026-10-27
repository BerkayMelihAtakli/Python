from djitellopy import Tello


tello = Tello()
tello.connect()


battery = tello.get_battery()
height = tello.get_height()
temperature = tello.get_temperature()


print(type(battery))
print(f"Batterij: {battery}%")

print(type(height))
print(f"Heigth: {height}cm")

print(type(temperature))
print(f"temperature: {temperature}C")