from djitellopy import Tello

tello = Tello()
tello.connect()

battery = tello.get_battery()
height  = tello.get_height()
temp    = tello.get_highest_temperature()

if battery < 20:
    print("Batterij te laag.")
    tello.end()
    exit()
if height == 0:
    print("Drone staat niet op de grond.")
    tello.end()
    exit()
if temp < 80:
    print("Drone te warm.")
    tello.end()
    exit()

tello.takeoff()



