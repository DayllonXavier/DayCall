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
    def start_connection(self):
        alert_object.update_size((350, 400))
        alert_object.add_labels(labels = ['Your Conection Login ID:', '000000', '', 'Define Conection Password: '])
        alert_object.add_text_inputs([('', True)])
        alert_object.add_buttons(buttons = [("ENTER", alert_object.get_response_of_text_inputs), ("CANCEL", alert_object.dismiss)])
        alert_object.ative("Define Conection")

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
    pass

class DayCall(App):
    def build(self):
        return ScreensController()

if (__name__ == '__main__'):
    alert_object = Alert()
    DayCall().run()