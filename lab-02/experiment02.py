import cv2
import time
import uuid
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

response = tello.get_battery()
print(f'Current drone battery: {response}%')

tello.streamon()

is_recording = True
frame_read = tello.get_frame_read()

def videoRecorder():
    
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter(f'{uuid.uuid1()}.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while is_recording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()
    
try:
    
	recorder = Thread(target=videoRecorder)
	recorder.start()

	tello.takeoff()
	tello.set_mission_pad_detection_direction(2)

	pad = tello.get_mission_pad_id()

	while pad != 1:

		print(pad)

		if pad == 4:
			tello.move_up(20)
			tello.rotate_counter_clockwise(90)

		if pad == 2:
			tello.rotate_clockwise(90)

		if pad == 8:
			tello.move_left(50)
			tello.move_down(20)

		if pad == 6:
			tello.move_right(50)
			tello.land()

		pad = tello.get_mission_pad_id()
  
except Exception:
	tello.disable_mission_pads()
	is_recording = False
	recorder.join()
 
finally:
	tello.disable_mission_pads()
	is_recording = False
	recorder.join()
