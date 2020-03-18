# using kv language to create same screen as gui.py

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    first = ObjectProperty(None)
    last = ObjectProperty(None)
    email = ObjectProperty(None)

    def submit_button(self):
        print("First Name: ", self.first.text)
        print("Last Name: ", self.last.text)
        print("Email: ", self.email.text)

        self.first.text = ""
        self.last.text = ""
        self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
