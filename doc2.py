import pandas as pd
from pynse import *
from tkinter import *
import psycopg2
from tkinter import ttk
import time
import datetime as dt
from tkinter import messagebox
from functools import lru_cache

# Cache for stock prices to reduce delay
@lru_cache(maxsize=100)
def get_stock_price(symbol):
    nse = Nse()
    return nse.get_quote(symbol)['lastPrice']

root = Tk()


def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()


root["bg"] = "black"
root.title('Login')
root["padx"] = 50
root["pady"] = 50

headinglabel = Label(root, text="Login", font="arial 20 bold",
                     bg="black", fg="#ffffff").grid(row=0, column=1)

labelemail = Label(root, text="Enter your email address",
                   font="arial 10 bold", bg="black", fg="#228B22")
labelemail.grid(row=1, column=0)


var1 = StringVar()
var2 = StringVar()

emailid = Entry(root, width=50, bg="#228B22", fg="yellow",
                borderwidth=10, font="arial 10 bold", textvariable=var1)
emailid.grid(row=1, column=1)
emailid.insert(0, "")
emailid.focus_set()

spacer1 = Label(root, text="", bg="black")
spacer1.grid(row=2, column=0)

labelpass = Label(root, text="Enter your password",
                  font="arial 10 bold", bg="black", fg="#228B22")
labelpass.grid(row=3, column=0)

passw = Entry(root, show="*", width=50, bg="#228B22", fg="yellow",
              borderwidth=10, font="arial 10 bold", textvariable=var2)
passw.grid(row=3, column=1)
passw.insert(0, "")

spacer2 = Label(root, text="", bg="black")
spacer2.grid(row=4, column=0)
displaytable = LabelFrame(root, text="test", bg="black",
                          fg="white", padx=10, pady=10).grid(row=10, column=1)



def myfun():
    global inp
    global inppass
    inp = var1.get()
    inppass = var2.get()
    try:
        ps_connection = psycopg2.connect(
            user=inp, password=inppass, host="127.0.0.1", port="5432", database="stocksdb2")
        cursor = ps_connection.cursor()
        cursor.execute("select * from account;")
        demat_number = StringVar()
        result = cursor.fetchall()
        demat_number = result[0][0]

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")
    clear_frame()
    controlroom(inp, inppass, demat_number)


submitbutton = Button(root, text="Submit", relief="groove", activeforeground="pink", activebackground="white",
                      font="arial 10 bold", padx=20, pady=5, command=myfun, fg="white", bg="#228B22", borderwidth=8).grid(row=5, column=1)

companylogin = Button(root, text="Company login", relief="groove", activeforeground="pink", activebackground="white",
                      font="arial 10 bold", padx=20, pady=5, command=myfun, fg="white", bg="#228B22", borderwidth=8).grid(row=6, column=2)
createnewaccount = Button(root, text="Create account", relief="groove", activeforeground="pink", activebackground="white",
                          font="arial 10 bold", padx=20, pady=5, command=myfun, fg="white", bg="#228B22", borderwidth=8).grid(row=6, column=0)



def controlroom(acc, passw, demat_number):
    homelabel = Label(root, text="Home", font="arial 25 bold",
                      bg="black", fg="white", padx=25, pady=20)
    homelabel.grid(row=0, column=1, columnspan=9)
    framehome = LabelFrame(root, text="Welcome", bg="black",
                           fg="white", padx=10, pady=10).grid(row=1, column=1)

    transactions_button = Button(framehome, text="Transaction details", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                                 padx=161, pady=5, command=lambda: afterlogin(f"select * from transactions ;", "transactions", acc, passw), fg="white", bg="#228B22")
    transactions_button.grid(row=1, column=1)

    a_shares_button = Button(framehome, text="Holdings", relief="groove", activeforeground="pink", activebackground="white",
                             font="arial 10 bold", padx=150, pady=5, command=lambda: afterlogin(f"select nse, sum(number_of_shares) as Quantity,share_price as LTP from a_shares, shares where nse_symbol=nse group by nse, share_price;", "a_shares", acc, passw), fg="white", bg="#228B22")
    a_shares_button.grid(row=2, column=1)

    company_button = Button(framehome, text="List Companies", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                            padx=153, pady=5, command=lambda: afterlogin(f"select * from company ;", "company", acc, passw), fg="white", bg="#228B22")
    company_button.grid(row=1, column=3)

    view_shares_button = Button(framehome, text="List Shares", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                                padx=166, pady=5, command=lambda: afterlogin(f"select * from shares ;", "shares", acc, passw), fg="white", bg="#228B22")
    view_shares_button.grid(row=2, column=3)

    buybutton = Button(framehome, text="Buy Shares", relief="groove", activeforeground="green", activebackground="black", font="arial 10 bold",
                       padx=185, pady=5, command=lambda: buyphase(acc, passw, demat_number, 'buy'), fg="white", bg="#DC143C")
    buybutton.grid(row=4, column=1)

    sell_button = Button(framehome, text="Sell shares", relief="groove", activeforeground="green", activebackground="black", font="arial 10 bold",
                         padx=168, pady=5, command=lambda: buyphase(acc, passw, demat_number, 'sell'), fg="white", bg="#DC143C")
    sell_button.grid(row=4, column=3)

    # Example usage of the cache
    stock_price = get_stock_price('RELIANCE')
    print(f'Reliance stock price: {stock_price}')  # This will use the cache

    root.mainloop()