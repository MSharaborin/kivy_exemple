from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton


class MyClass(Screen):

     def __init__(self, **kwargs):
         super(MyClass, self).__init__(**kwargs)
         self.add_widget(MDRectangleFlatButton(text='Ok', pos_hint={"center_x": 0.4, "center_y": 0.5},))
         self.add_widget(MDRectangleFlatButton(text='Cancel', pos_hint={"center_x": 0.6, "center_y": 0.5},))


class MainApp(MDApp):
    def build(self):
        screen = MyClass()
        return screen


MainApp().run()