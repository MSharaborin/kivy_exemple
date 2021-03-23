import kivy
from kivy.properties import ObjectProperty
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App


class AccordionApp(App):

    test = ObjectProperty()

    def build(self):
        root = Accordion()
        for x in range(5):
            item = AccordionItem(title='Title %d' % x)
            item.add_widget(self.test)
            root.add_widget(item)
        return root


if __name__ == '__main__':
    AccordionApp().run()