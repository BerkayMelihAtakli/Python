from djitellopy import Tello


MIN_BATTERY = 20
MAX_TEMP = 65
MAX_HEIGHT = 200

tello = Tello()
tello.connect()

battery = tello.get_battery()
temp    = tello.get_highest_temperature()
height  = tello.get_height()


if battery < MIN_BATTERY:
    print(f"Battery too low: {battery}% (minimum required: {MIN_BATTERY}%)")
    tello.end()
    exit()


if temp > MAX_TEMP:
    print(f"Temperature too high: {temp}°C (maximum allowed: {MAX_TEMP}°C)")
    tello.end()
    exit()


if height > MAX_HEIGHT:
    print(f"Starting height too high: {height} cm (maximum allowed: {MAX_HEIGHT} cm)")
    tello.end()
    exit()


tello.takeoff()