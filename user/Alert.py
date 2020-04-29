# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class Alert(object):
    def __init__(self):
        self.alert = None
    
    def construct_mensage(self, title = 'ALERT', labels = [], images = [], buttons = [], 
                                font_size = 20, color_text = (1, 1, 1, 1), size = (350, 200)):
        contentPopup = BoxLayout(orientation = 'vertical')
        contentBodyPopup = BoxLayout(orientation = 'vertical', size_hint_y = 0.5, spacing = 10, padding = 10)

        for image in images:
            contentBodyPopup.add_widget(Image(source = image[0], height = image[1], allow_stretch = True, size_hint_y = None))

        for label in labels:
            contentBodyPopup.add_widget(Label(text = label, font_size = font_size, bold = False, color = color_text))

        contentButtonsPopup = BoxLayout(orientation = 'horizontal', spacing = 10, padding = 5, size_hint_y = 0.35)
        for button in buttons:
            contentButtonsPopup.add_widget(Button(text = button[0], on_release = button[1]))

        contentPopup.add_widget(BoxLayout(size_hint_y = 0.05))
        contentPopup.add_widget(contentBodyPopup)
        contentPopup.add_widget(BoxLayout(size_hint_y = 0.1))
        contentPopup.add_widget(contentButtonsPopup)

        self.alert = Popup(title = title, content = contentPopup, size_hint = (None, None), size = size)
    
    def ative(self, *args):
        if (self.alert == None):
            print("no alert built")
            return
        self.alert.open()
    
    def dismiss(self, *args):
        if (self.alert == None):
            print("no alert built")
            return
        self.alert.dismiss()
    