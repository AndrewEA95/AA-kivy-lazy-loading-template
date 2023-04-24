from kivy.uix.screenmanager import Screen
from .file_It import fileapp

class mk_file(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.shared = fileapp()
                
    def change_screen(self):
        sharedV = self.shared.shared_v
        print(sharedV)
        self.manager.set_current("dropO")
