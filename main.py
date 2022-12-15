__author__ = 'bunkus'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import logging

import cv2

try:
 from android.permissions import request_permissions, Permission
 request_permissions([
 Permission.CAMERA,
 Permission.WRITE_EXTERNAL_STORAGE,
 Permission.READ_EXTERNAL_STORAGE,
 Permission.INTERNET,
 Permission.BODY_SENSORS,
 Permission.BLUETOOTH
 ])
except Exception as e:
 logging.warn(e)


class CamApp(App):

    def build(self):
        # define a video capture object
        vid = cv2.VideoCapture(0)

        while(True):
      
           # Capture the video frame
           # by frame
           ret, frame = vid.read()
  
           # Display the resulting frame
           cv2.imshow('frame', frame)
      
           # the 'q' button is set as the
           # quitting button you may use any
           # desired button of your choice
           if cv2.waitKey(1) & 0xFF == ord('q'):
               break
  
        # After the loop release the cap object
        vid.release()   



if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()
