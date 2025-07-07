from djitellopy import Tello

tello = Tello()
tello.connect()

power = tello.get_battery()
print("Power Level =", power,"%")
tello.takeoff()
tello.land()