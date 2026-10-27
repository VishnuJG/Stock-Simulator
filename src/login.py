from tkinter import *
import psycopg2
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root['bg'] = 'black'
        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text='Enter your email address', bg='black', fg='#228B22').grid(row=0, column=0)
        self.email_var = StringVar()
        Entry(self.root, textvariable=self.email_var, bg='#228B22', fg='yellow').grid(row=0, column=1)

        Label(self.root, text='Enter your password', bg='black', fg='#228B22').grid(row=1, column=0)
        self.password_var = StringVar()
        Entry(self.root, textvariable=self.password_var, show='*', bg='#228B22', fg='yellow').grid(row=1, column=1)

        Button(self.root, text='Submit', command=self.login).grid(row=2, column=1)

    def login(self):
        email = self.email_var.get()
        password = self.password_var.get()
        # Database connection and validation logic here
        # On success, transition to the main application

if __name__ == '__main__':
    root = Tk()
    app = LoginApp(root)
    root.mainloop()