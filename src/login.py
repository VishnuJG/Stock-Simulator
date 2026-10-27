from tkinter import *
import psycopg2
from tkinter import ttk

class StockSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title('Stock Simulator')
        self.root['bg'] = 'black'
        self.create_login_frame()

    def create_login_frame(self):
        self.login_frame = LabelFrame(self.root, text='Login', bg='black', fg='white', padx=10, pady=10)
        self.login_frame.pack(padx=10, pady=10)

        Label(self.login_frame, text='Enter your email address', font='arial 10 bold', bg='black', fg='#228B22').grid(row=1, column=0)
        self.email_var = StringVar()
        Entry(self.login_frame, width=50, bg='#228B22', fg='yellow', borderwidth=10, font='arial 10 bold', textvariable=self.email_var).grid(row=1, column=1)

        Label(self.login_frame, text='Enter your password', font='arial 10 bold', bg='black', fg='#228B22').grid(row=3, column=0)
        self.password_var = StringVar()
        Entry(self.login_frame, show='*', width=50, bg='#228B22', fg='yellow', borderwidth=10, font='arial 10 bold', textvariable=self.password_var).grid(row=3, column=1)

        Button(self.login_frame, text='Submit', relief='groove', activeforeground='pink', activebackground='white', font='arial 10 bold', padx=20, pady=5, command=self.login, fg='white', bg='#228B22').grid(row=5, column=1)

    def login(self):
        email = self.email_var.get()
        password = self.password_var.get()
        # Add login logic here

if __name__ == '__main__':
    root = Tk()
    app = StockSimulator(root)
    root.mainloop()