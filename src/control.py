from tkinter import *
import psycopg2

class ControlRoom:
    def __init__(self, root, acc, passw):
        self.root = root
        self.acc = acc
        self.passw = passw
        self.create_widgets()

    def create_widgets(self):
        self.frame_home = LabelFrame(self.root, text='Welcome', bg='black', fg='white', padx=10, pady=10)
        self.frame_home.pack()

        Button(self.frame_home, text='Transaction details', command=self.show_transactions, bg='#228B22', fg='white').pack()
        Button(self.frame_home, text='Account shares details', command=self.show_account_shares, bg='#228B22', fg='white').pack()
        Button(self.frame_home, text='List Companies', command=self.list_companies, bg='#228B22', fg='white').pack()

    def show_transactions(self):
        # Implement transaction details logic
        pass

    def show_account_shares(self):
        # Implement account shares details logic
        pass

    def list_companies(self):
        # Implement list companies logic
        pass