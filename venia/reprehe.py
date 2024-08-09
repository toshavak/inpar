from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class TapWidget(Widget):
    def __init__(self, **kwargs):
        super(TapWidget, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0)  # initial color is red
            self.ellipse = Ellipse(pos=(100, 100), size=(50, 50))

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            with self.canvas:
                if self.ellipse.color == (1, 0, 0, 1):
                    self.ellipse.color = (0, 0, 1, 1)  # blue
                else:
                    self.ellipse.color = (1, 0, 0, 1)  # red

class TapCircleApp(App):
    def build(self):
        return TapWidget()

if __name__ == '__main__':
    TapCircleApp().run()
