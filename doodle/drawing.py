# Drawing app
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(255, 255, 255, mode='rgb')
            self.line = Line(points=())

    def on_touch_down(self, touch):
        self.line.points = tuple()

    def on_touch_move(self, touch):
        self.line.points += touch.pos


class DrawingApp(App):
    def build(self):
        return Touch()


if __name__ == '__main__':
    DrawingApp().run()
