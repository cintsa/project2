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

        if(vid.isOpened()==False):
         print("Error opening video")


        while(vid.isOpened()):
      
           # Capture the video frame
           # by frame
           ret, frame = vid.read()
           if(ret==True):  
             # Display the resulting frame
             #cv2.imshow('frame', frame)  
 
             if cv2.waitKey(25) & 0xFF == ord('q'):
               break
           else:
             break
  
        # After the loop release the cap object
        vid.release()   



if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()
