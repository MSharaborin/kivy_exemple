import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.pagelayout import PageLayout


class PageLayout(PageLayout):
    pass


class PageLayoutApp(App):

    def build(self):
        return PageLayout()

if __name__ == '__main__':
    PageLayoutApp().run()