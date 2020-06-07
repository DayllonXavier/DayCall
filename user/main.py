# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock

import threading

from Alert import Alert
from CameraCapture import CameraCapture
from Connection import Connection

class ScreensController(ScreenManager):
    def start_screen_home(self, *args):
        self.current = 'ScreenHome'
    def start_screen_call(self, *args):
        self.current = 'ScreenCall'

class ScreenHome(Screen):
    def start_connection(self):
        alert_object.update_size((350, 400))
        alert_object.add_labels(labels = ['Your Conection Login ID:', '000000', '', 'Define Conection Password: '])
        alert_object.add_text_inputs([('', True)])
        alert_object.add_buttons(buttons = [("ENTER", self.manager.start_screen_call), ("CANCEL", alert_object.dismiss)])
        alert_object.ative("Define Connection")

    def enter_a_conection(self):
        alert_object.update_size((350, 400))
        alert_object.add_labels(labels = ['Conection Login ID: '])
        alert_object.add_text_inputs([('', False)])
        alert_object.add_labels(labels = ['Conection Password: '])
        alert_object.add_text_inputs([('', True)])
        alert_object.add_buttons(buttons = [("ENTER", alert_object.get_response_of_text_inputs), ("CANCEL", alert_object.dismiss)])
        alert_object.ative("Access Conection")
    
    def more_informations(self):
        alert_object.construct_mensage(labels = ['Software developed by:', 'Dayllon Xavier', '', 'For more information access:', 'github.com/DayllonXavier/DayCall'], buttons = [('RETURN', alert_object.dismiss)], size = (400, 300))
        alert_object.ative('More Informations')

    def confirm_exit(self):
        alert_object.construct_mensage(labels = ['You really want to leave?'], buttons = [('YES', App.get_running_app().stop), ('NO', alert_object.dismiss)])
        alert_object.ative()

class ScreenCall(Screen):
    def on_pre_enter(self):
        self.separate = "{||}".encode('utf-8')
        self.partition_size = 1000
        self.connected = True
        self.clock_atualize_images = None
        self.fps = 30
        camera_object.init_capture()
        self.your_image = None
        self.other_image = None
        connection_object.udp_socket_init()
        connection_object.udp_socket_connect(('127.0.0.1', 1060)) #Address temp
        self.init_clock_atualize_images()

    def init_clock_atualize_images(self, *args):
        self.stop_clock_atualize_images()
        self.clock_atualize_images = Clock.schedule_interval(self.update_images, 1.0/self.fps)
    
    def stop_clock_atualize_images(self, *args):
        if (self.clock_atualize_images is not None):
            self.clock_atualize_images.cancel()

    def update_images(self, *args):
        self.your_image, size = camera_object.get_string_image()

        if (self.other_image is None):
            self.other_image = self.your_image
            threading.Thread(target = self.recv_other_image).start()

        #threading.Thread(target = self.send_your_image, args = (self.your_image,)).start()
        self.send_your_image(self.your_image)

        your_texture_image = Texture.create(size = size, colorfmt='bgr')
        your_texture_image.blit_buffer(self.your_image, colorfmt='bgr', bufferfmt='ubyte')

        other_texture_image = Texture.create(size = size, colorfmt='bgr')
        other_texture_image.blit_buffer(self.other_image, colorfmt='bgr', bufferfmt='ubyte')

        self.alter_images(your_texture_image, other_texture_image)

    def alter_images(self, your_image, other_image):
        self.ids.your_image.texture = your_image
        self.ids.other_image.texture =  other_image

    def close_connection(self):
        self.stop_clock_atualize_images()
        camera_object.destroy_capture()
        self.connected = False
        self.manager.start_screen_home()

    def send_your_image(self, image, *args):
        size = (len(image) // self.partition_size) + (len(image) % self.partition_size != 0)
        for i in range(0, size):
            left_border = i * self.partition_size
            right_border = min(left_border + self.partition_size, len(image))
            data = str(left_border).encode('utf-8') + self.separate + image[left_border : right_border]
            print("SIZE DATA: {}".format(len(data)))
            connection_object.udp_socket_send_bytes(data = data)
    
    def recv_other_image(self):
        print("INIT")
        while(self.connected):
            data = connection_object.udp_socket_recv_bytes()
            if (data is not None):
                data = data.split(self.separate)
                if (len(data) != 2):
                    continue
                data[0] = int(data[0].decode('utf-8'))
                left_border = data[0] * self.partition_size
                self.other_image = self.other_image[: left_border] + data[1] + self.other_image[left_border + len(data[1]) :]


class DayCall(App):
    def build(self):
        return ScreensController()

if (__name__ == '__main__'):
    alert_object = Alert()
    camera_object = CameraCapture()
    connection_object = Connection()
    DayCall().run()