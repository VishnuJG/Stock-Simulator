from tkinter import *
from login import LoginApp

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Stock Simulator')
        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text='Welcome to Stock Simulator', font='Arial 20 bold').pack()
        # Additional widgets for the main application

if __name__ == '__main__':
    root = Tk()
    app = MainApp(root)
    root.mainloop()