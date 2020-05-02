# -*- coding: utf-8 -*-

import cv2

class CameraCapture(object):
    def __init__(self, width = 640, height = 480):
        self.size = (width, height)
        self.buffer = None
        self.stringBuffer = None
    
    def init_capture(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.size[1])
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.size[0])

    def destroy_capture(self):
        self.capture.release()

    def capture_image(self):
        ret, frame = self.capture.read()
        frame = cv2.flip(frame, -1)
        self.buffer = frame
    
    def transform_string(self):
        self.stringBuffer = self.buffer.tostring()
    
    def get_string_image(self):
        self.capture_image()
        self.transform_string()
        return (self.stringBuffer, self.size)

    def test_camera(self):
        while (True):
            ret, frame = self.capture.read()
            frame = cv2.flip(frame, 1)
            cv2.imshow('video1', frame)

            if (cv2.waitKey(1) & 0xff == ord('q')):
                break
        cv2.destroyAllWindows()