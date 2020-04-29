# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class ScreensController(ScreenManager):
    def start_screen_home(self):
        self.current = 'ScreenHome'
    def start_screen_call(self):
        self.current = 'ScreenCall'

class ScreenHome(Screen):
    pass

class ScreenCall(Screen):
    pass

class CallDay(App):
    def build(self):
        return ScreensController()

if (__name__ == '__main__'):
    CallDay().run()