# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

from Alert import Alert

class ScreensController(ScreenManager):
    def start_screen_home(self):
        self.current = 'ScreenHome'
    def start_screen_call(self):
        self.current = 'ScreenCall'

class ScreenHome(Screen):
    def confirm_exit(self):
        alert_object.construct_mensage(labels = ['You really want to leave?'], buttons = [('YES', App.get_running_app().stop), ('NO', alert_object.dismiss)])
        alert_object.ative()

class ScreenCall(Screen):
    pass

class DayCall(App):
    def build(self):
        return ScreensController()

if (__name__ == '__main__'):
    alert_object = Alert()
    DayCall().run()