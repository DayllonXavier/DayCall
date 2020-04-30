# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

class Alert(object):
    def __init__(self, size = (350, 200)):
        self.size = size
        self.alert = None
        self.contentBodyPopup = None
        self.contentButtonsPopup = None
        self.textInputs = []
        self.reponseOfTextInput = []
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
                                padding = padding, size_hint_y = None, height = height, size = (self.size[0], height))

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
    
    def add_text_inputs(self, text_inputs = [], font_size = 20, color_text = (1, 1, 1, 1,), font_family = 'sans-serif', height = 48, padding = 10):
        self.create_contentBodyPopup()
        for text_input in text_inputs:
            self.textInputs.append(TextInput(text=text_input[0], password = text_input[1], font_family = font_family, font_size = font_size, 
                                    padding = padding, height = height, size_hint_y = None, multiline = False))
            self.contentBodyPopup.add_widget(self.textInputs[-1])
    
    def construct(self, title = "ALERT", *args):
        if (self.contentBodyPopup is not None):
            self.alert.content.add_widget(self.contentBodyPopup)
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
    
    def get_response_of_text_inputs(self, *args):
        self.reponseOfTextInput = []
        for text_input in self.textInputs:
            self.reponseOfTextInput.append(text_input.text)
        self.textInputs = []
        #print(self.response_of_text_inputs())
        self.dismiss()

    def response_of_text_inputs(self, *args):
        return list(self.reponseOfTextInput)