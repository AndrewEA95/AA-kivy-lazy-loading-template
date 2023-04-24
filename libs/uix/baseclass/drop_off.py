from kivy.uix.screenmanager import Screen

class dropOff(Screen):
    def show_filechooser(self):
        self.ids.filechooser_popup.open()

    def file_selected(self, selection):
        # Handle selected files
        print(f"Selected files: {selection}")
        self.ids.filechooser_popup.dismiss()

    def change_screen(self):
        self.manager.set_current("pickF")
