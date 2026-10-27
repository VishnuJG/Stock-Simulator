from tkinter import *
from database import Database

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title('Stock Simulator')
        self.create_main_frame()

    def create_main_frame(self):
        self.main_frame = Frame(self.root)
        self.main_frame.pack()
        # Add UI components here

if __name__ == '__main__':
    root = Tk()
    app = UI(root)
    root.mainloop()