import cv2
import numpy as np
from time import time



class Camera(object):
    # ...
    last_access = 0  # time of last client access to the camera

    # ...

    def get_frame(self):
        Camera.last_access = time.time()
        # ...

    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:
            # ...
            for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                # ...
                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
                if time.time() - cls.last_access > 10:
                    break
        cls.thread = None