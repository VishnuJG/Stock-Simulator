from tkinter import *
import psycopg2
from tkinter import ttk

root = Tk()

def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()

loginframe = LabelFrame(root, text="Login", bg="black",
                        fg="white", padx=10, pady=10)
loginframe.pack(padx=10, pady=10)

labelemail = Label(loginframe, text="Enter your email address",
                   font="arial 10 bold", bg="black", fg="#228B22")
labelemail.grid(row=1, column=0)

var1 = StringVar()
var2 = StringVar()

emailid = Entry(loginframe, width=50, bg="#228B22", fg="yellow",
                borderwidth=10, font="arial 10 bold", textvariable=var1)
emailid.grid(row=1, column=1)
emailid.insert(0, "")
emailid.focus_set()

labelpass = Label(loginframe, text="Enter your password",
                  font="arial 10 bold", bg="black", fg="#228B22")
labelpass.grid(row=3, column=0)

passw = Entry(loginframe, show="*", width=50, bg="#228B22", fg="yellow",
              borderwidth=10, font="arial 10 bold", textvariable=var2)
passw.grid(row=3, column=1)
passw.insert(0, "")


def myfun():
    inp = var1.get()
    inppass = var2.get()
    loginframe.pack_forget()
    controlroom(inp, inppass)

submitbutton = Button(loginframe, text="Submit", relief="groove", activeforeground="pink", activebackground="white",
                      font="arial 10 bold", padx=20, pady=5, command=myfun, fg="white", bg="#228B22")
submitbutton.grid(row=5, column=1)


def controlroom(acc, passw):
    # Functionality to handle user actions in the main interface after login
    pass

root.mainloop()
