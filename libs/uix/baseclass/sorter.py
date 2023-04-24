# what I'll need is how many folders to be made and then the names of the folders
# then I can sort the files that are made so what willneed to be done is 
# I will need to change how the code gets the files as the user won't need to put anything in 
# I don't think, then I will need to replace it with the files made by the user
# then we will have to figure out how to sort the files either one by one or
# getting all of the files then sorting them after


import os
import fitz
# import glob
import shutil
# import docx
# import PyPDF2
# from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup

class FileSorterGUI(Screen):
    # def __init__(self, **kwargs):
    #     super(FileSorterGUI, self).__init__(**kwargs)
    def sort_file_paths(self):
        return self.ids.files_path.text, self.ids.output_dir.text
    
    def get_file_type(self):
        return self.ids.file_types.text.split(",")

    def get_keywords(self, files_to_view):
        keys = self.ids.keywords.text
        
        # try:
        #     with open(files_to_view, "r"):
        #         matching_files = [line for line in files_to_view if keys in line]
                
        #         if matching_files:
        #             return True
                
        #         else:
        #             return False
        
        # except IOError:
        #     pass
         # Open the PDF file
          # Open the PDF file
        with fitz.open(files_to_view) as pdf_file:
            # Iterate over each page in the PDF file
            for page_num in range(pdf_file.page_count):
                # Get the page object
                page = pdf_file[page_num]
                
                # Extract the text from the page
                page_text = page.get_text()
                
                # Check if the keyword is in the page text
                for keyword in self.ids.keywords.text.split(","):
                    if keyword in page_text:
                        print(f"Keyword '{keyword}' found on page {page_num + 1}")
                        return True
        return False
    def makeFiles(self):
        # Create a new folder called "my_folder"
        folder_name = "my_folder"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
    
    def sort_files(self):
        # file = "/users/andrewanglin/Downloads/"
        # file1 = "/users/andrewanglin/documents/pdf_files"
        file, file1 =  FileSorterGUI.sort_file_paths(self)

        fileType = tuple(FileSorterGUI.get_file_type(self))
        
        allfiles = os.listdir(file)
        
        for f in allfiles:
            if f.endswith(fileType):
              if FileSorterGUI.get_keywords(self, os.path.join(file, f)):
                src_path = os.path.join(file, f)
                dest_path = os.path.join(file1, f)
                shutil.move(src_path, dest_path)
                popup = Popup(title='Success', content=Label(text='Files sorted successfully!'), size_hint=(None, None), size=(200, 200))
                popup.open()
            else:
                popup = Popup(title='Failed', content=Label(text='No matching results'), size_hint=(None, None), size=(200, 200))
                popup.open()

if __name__ == '__main__':
    FileSorterGUI().run()