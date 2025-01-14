from kivymd.app import MDApp
from kivy.core.window import Window

from libs.uix.root import Root


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = "File-it_V2"

        Window.keyboard_anim_args = {"d": 0.2, "t": "linear"}
        Window.softinput_mode = "below_target"

    def build(self):
        self.root = Root()
        self.root.set_current("appit")


if __name__ == "__main__":
    MainApp().run()
