# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class Alert(object):
    def __init__(self, size = (350, 200)):
        self.size = size
        self.alert = None
        self.contentBodyPopup = None
        self.contentButtonsPopup = None
        self.init_alert()

    def init_alert(self, spacing = 10, padding = 10):
        self.alert = Popup(content = BoxLayout(orientation = 'vertical', spacing = spacing,
                           padding = padding), size_hint = (None, None), size = self.size)

    def update_size(self, size = (350, 200)):
        self.size = size
        self.alert.size = size
    
    def create_contentBodyPopup(self, spacing = 10, padding = 10):
        if (self.contentBodyPopup is None):
            self.contentBodyPopup = BoxLayout(orientation = 'vertical', spacing = spacing, padding = padding)

    def create_contentButtonsPopup(self, height = 50, spacing = 10, padding = 5):
        if (self.contentButtonsPopup is None):
            self.contentButtonsPopup = BoxLayout(orientation = 'horizontal', spacing = spacing, 
                                padding = padding, size_hint_y = None, size = (self.size[0], height))

    def add_labels(self, labels = [], font_size = 20, color_text = (1, 1, 1, 1)):
        self.create_contentBodyPopup()
        for label in labels:
            self.contentBodyPopup.add_widget(Label(text = label, font_size = font_size, color = color_text, bold = False))
    
    def add_images(self, images = []):
        self.create_contentBodyPopup()
        for image in images:
            self.contentBodyPopup.add_widget(Image(source = image[0], height = image[1], allow_stretch = True, size_hint_y = None))

    def add_buttons(self, buttons = [], font_size = 20, color_text = (1, 1, 1, 1)):
        self.create_contentButtonsPopup()
        for button in buttons:
            self.contentButtonsPopup.add_widget(Button(text = button[0], on_release = button[1]))
    
    def construct(self, title = "ALERT", *args):
        self.alert.content.add_widget(BoxLayout(size_hint_y = None, size = (self.size[0], 20)))
        if (self.contentBodyPopup is not None):
            self.alert.content.add_widget(self.contentBodyPopup)
        self.alert.content.add_widget(BoxLayout(size_hint_y = None, size = (self.size[0], 20)))
        if (self.contentButtonsPopup is not None):
            self.alert.content.add_widget(self.contentButtonsPopup)
        self.alert.title = title

    def deconstruct(self, *args):
        self.init_alert()
        self.contentBodyPopup = None
        self.contentButtonsPopup = None

    def ative(self, title = "ALERT", *args):
        self.construct(title = title)
        self.alert.open()
    
    def dismiss(self, *args):
        self.alert.dismiss()
        self.deconstruct()

    def construct_mensage(self, labels = [], images = [], buttons = [], font_size = 20, color_text = (1, 1, 1, 1), size = (350, 200)):
        self.update_size(size)
        self.add_images(images = images)
        self.add_labels(labels = labels, color_text = color_text, font_size = font_size)
        self.add_buttons(buttons = buttons, font_size = font_size, color_text = color_text)
        