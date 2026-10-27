from tkinter import *
from tkinter import ttk
import psycopg2

class StockSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title('Stock Simulator')
        self.root.configure(bg='black')
        self.create_login_frame()

    def create_login_frame(self):
        self.login_frame = LabelFrame(self.root, text='Login', bg='black', fg='white', padx=10, pady=10)
        self.login_frame.pack(padx=10, pady=10)

        Label(self.login_frame, text='Email:', bg='black', fg='#228B22').grid(row=0, column=0)
        self.email_entry = Entry(self.login_frame, width=50, bg='#228B22', fg='yellow')
        self.email_entry.grid(row=0, column=1)

        Label(self.login_frame, text='Password:', bg='black', fg='#228B22').grid(row=1, column=0)
        self.password_entry = Entry(self.login_frame, show='*', width=50, bg='#228B22', fg='yellow')
        self.password_entry.grid(row=1, column=1)

        Button(self.login_frame, text='Submit', command=self.login, bg='#228B22', fg='white').grid(row=2, columnspan=2)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        # Implement login logic here

if __name__ == '__main__':
    root = Tk()
    app = StockSimulator(root)
    root.mainloop()