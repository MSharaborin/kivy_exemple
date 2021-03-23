from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class Error(GridLayout):

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.cols = 1


class ApplicationMAin(GridLayout):

    def __init__(self, **kwargs):
        super(ApplicationMAin, self).__init__(**kwargs)
        self.cols = 2
        self.val = 0

    def on_click_ok(self, *args):
        print(self.count_text.text)
        if self.count_text.text:
            # Clock.schedule_interval(self.on_click_ok, 1)
            for _ in range(int(self.count_text.text)):
                print(_)
                self.add_widget(Label(text=self.input_text.text))
        else:
            self.show_popup()

    def canceled(self, *args):
        self.label_total.text = f'Total: {str(self.val)}'
        Clock.unschedule(self.on_click_ok)

    def show_popup(self, *args):
        show = Error()
        self.popup = Popup(title ="TypeError", content=show,
                      size_hint=(None, None), size=(500, 200))
        self.popup.open()


class ApplicationMAinApp(App):

    def build(self):
        return ApplicationMAin()


if __name__ == '__main__':
    ApplicationMAinApp().run()