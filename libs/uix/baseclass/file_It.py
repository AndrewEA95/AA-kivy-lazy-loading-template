from kivy.uix.screenmanager import Screen

from .dataM import DataManager

# class share():
#     def __init__(self) -> None:
#         super().__init__()
#         # self.data = DataManager()
#         self.shared_v = None
class fileapp(Screen): 
    # def __init__(self) -> None:
    #     super().__init__()
    #     # self.data = DataManager()
    #     self.shared_v = None
    def change_screen(self):
        # work on what this code does
        # app.root.current = 'file_creator_screen'; app.root.get_screen('file_creator_screen').file_count = int(file_count_input.text)
        # app.root.get_screen('another_screen').file_count = self.file_count
        # app = MDApp.get_running_app()
        # file_count = app.file_count
        # app.root.get_screen('another_screen').label.text = 'Number of files to create: {}'.format(file_count)
        # app.root.current = 'another_screen'
        
        self.shared_v = self.ids.mk_folder.text
        print(self.shared_v)
        self.manager.set_current("makeAFile")
