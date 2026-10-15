from djitellopy import Tello

tello = Tello()
tello.connect()

battery = tello.get_battery()               # percentage
temp    = tello.get_highest_temperature()   # graden Celsius
height  = tello.get_height()                # centimeters