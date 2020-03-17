# Hello World app to check if packages and dependencies are installed correctly
# App will display a label with the text "Hello World!"
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        return Label(text="Hello World!")


if __name__ == '__main__':
    MyApp().run()
