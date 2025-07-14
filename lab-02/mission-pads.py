from djitellopy import Tello

# create and connect
tello = Tello()
tello.connect()
power = tello.get_battery()
print("Power Level =", power,"%")
# configure drone
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)  # Forward & Backward

tello.takeoff()

pad = tello.get_mission_pad_id()

# detect and react to pads until we see pad #1
while pad != 1:
    if pad == 4:
        tello.move_back(30)
        tello.move_right(90)

    if pad == 2:
        tello.move_up(30)
        tello.rotate_clockwise(90)

    if pad == 8:
        tello.move_down(30)
        tello.rotate_counter_clockwise(90)

    if pad == 5:
        tello.land()

    pad = tello.get_mission_pad_id()

# termination
tello.disable_mission_pads()
tello.land()

tello.end()
