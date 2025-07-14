import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()
power = tello.get_battery()
print("Power Level =", power,"%")
tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
tello.move_up(30)

cv2.imwrite("picture21.png", frame_read.frame)
tello.land()