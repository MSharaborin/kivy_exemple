from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config

import json


class Error(GridLayout):

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.cols = 1


class ApplicationMAin(GridLayout):

    def __init__(self, **kwargs):
        super(ApplicationMAin, self).__init__(**kwargs)
        self.cols = 2
        self.val = 0
        self.read_config()

    def on_click_ok(self, *args):
        self.save_config()
        if self.count_text.text:
            # Clock.schedule_interval(self.on_click_ok, 1)
            for _ in range(int(self.count_text.text)):
                self.bat = Label(text=self.input_text.text + str(_))
                self.add_widget(self.bat)
        else:
            self.show_popup()

    def canceled(self, *args):
        self.label_total.text = f'Total: {str(self.count_text.text)}'
        if len(self.children) > 6:
            ct = int(len(self.children)) - 6
            for child in self.children[:ct]:
                self.remove_widget(child)
        # Clock.unschedule(self.on_click_ok)

    def show_popup(self, *args):
        show = Error()
        self.popup = Popup(title ="TypeError", content=show,
                      size_hint=(None, None), size=(500, 200))
        self.popup.open()

    def save_config(self, *args):
        data = {}
        data['count'] = self.count_text.text
        data['text'] = self.input_text.text
        with open("save.json", "w") as write_file:
            json.dump(data, write_file)

    def read_config(self, *args):
        with open('save.json', 'r') as read_file:
            data = json.load(read_file)
            self.count_text.text = data.get('count', None)
            self.input_text.text = data.get('text', None)


class ApplicationMAinApp(App):
    def build(self):
        return ApplicationMAin()


if __name__ == '__main__':
    ApplicationMAinApp().run()