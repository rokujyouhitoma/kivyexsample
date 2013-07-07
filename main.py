import kivy

from kivy.app import App
from kivy.uix.abstractview import AbstractView
from kivy.graphics import Color, Rectangle

class GameView(AbstractView):
    def __init__(self, **kwargs):
        super(AbstractView, self).__init__(**kwargs)
        self.run()

    def run(self):
        self.canvas.clear()
        with self.canvas:
            Color(1., 0, 0)
            Rectangle(pos=(10, 10), size=(500, 500))

    def on_touch_down(self, touch):
        print(touch.pos)

class GameConfig(object):
    configuration = {
        'title': 'sample game :)'
    }

class Application(App):

    def __init__(self, widget_class, conf_class):
        super(Application, self).__init__()
        self.conf = conf_class()
        self.setup_conf(self.conf.configuration)
        self.widget = widget_class()

    def setup_conf(self, conf):
        for key in conf.keys():
            self.setup_conf_one(key, conf[key])

    def setup_conf_one(self, key, value):
        setattr(self, key, value)

    def build(self):
        return self.widget

if __name__ == '__main__':
    Application(GameView, GameConfig).run()
