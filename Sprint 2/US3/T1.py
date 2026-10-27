from djitellopy import Tello

tello = Tello()
tello.connect()
battery = tello.get_battery()

# TODO: voeg guard clause toe
if battery < 20:
    print(f"Batterij te laag {battery}%")
    exit()


tello.takeoff()
tello.move_forward(100)
tello.land()
tello.end()