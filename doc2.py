import pandas as pd
from pynse import *
from tkinter import *
import psycopg2
from tkinter import ttk
import time
import datetime as dt
from tkinter import messagebox

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
        messagebox.showerror(title="Error", message=error)

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

    spacer3 = Label(root, text="", bg="black", padx=10)
    spacer3.grid(row=1, column=2)
    spacer4 = Label(root, text="", bg="black", padx=10)
    spacer4.grid(row=2, column=2)
    company_button = Button(framehome, text="List Companies", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                            padx=153, pady=5, command=lambda: afterlogin(f"select * from company ;", "company", acc, passw), fg="white", bg="#228B22")
    company_button.grid(row=1, column=3)

    view_shares_button = Button(framehome, text="List Shares", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                                padx=166, pady=5, command=lambda: afterlogin(f"select * from shares ;", "shares", acc, passw), fg="white", bg="#228B22")
    view_shares_button.grid(row=2, column=3)

    viewevents = Button(framehome, text="Events", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                        padx=181, pady=5, command=lambda: afterlogin(f"select * from events ;", "companies", acc, passw), fg="white", bg="#228B22")
    viewevents.grid(row=3, column=3)

    buybutton = Button(framehome, text="Buy Shares", relief="groove", activeforeground="green", activebackground="black", font="arial 10 bold",
                       padx=185, pady=5, command=lambda: buyphase(acc, passw, demat_number, 'buy'), fg="white", bg="#DC143C")
    buybutton.grid(row=4, column=1)

    accountdetails = Button(framehome, text="Account details", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                            padx=172, pady=5, command=lambda: afterlogin(f"select * from account ;", "account", acc, passw), fg="white", bg="#228B22")
    accountdetails.grid(row=3, column=1)

    sell_button = Button(framehome, text="Sell shares", relief="groove", activeforeground="green", activebackground="black", font="arial 10 bold",
                         padx=168, pady=5, command=lambda: buyphase(acc, passw, demat_number, 'sell'), fg="white", bg="#DC143C")
    sell_button.grid(row=4, column=3)


def buyphase(acc, passw, demat_number, ordertype):
    spacer1 = Label(root, text="", bg="black")
    spacer1.grid(row=0, column=0)
    try:
        global buyframe
        buyframe.grid_forget()
    except Exception as e:
        print(e)

    buyframe = LabelFrame(root, text="Welcome", bg="grey",
                          fg="white", padx=10, pady=10, font="arial 10 bold").grid(row=0, column=5)
    buylabel = Label(
        buyframe, text=f"Enter number of shares to {ordertype}", font="arial 15 bold", bg="black", fg="#228B22")
    buylabel.grid(row=12, column=1)
    quant = StringVar()
    buyamt = Entry(buyframe, bg="#228B22", fg="yellow",
                   borderwidth=10, font="arial 15 bold", textvariable=quant)
    buyamt.grid(row=12, column=2, columnspan=4)
    options = ['Select', 'RELIANCE', 'TCS', 'HDFCBANK',
               'INFY', 'HINDUNILVR', 'SBIN', 'WIPRO']
    temp = ['Select']
    if ordertype == "sell":
        res = adminlistofshares(
            acc, passw, "select distinct nse from a_shares;")
        print(res)
        for i in res:
            temp.append(i[0])
        options = temp
    clicked = StringVar()
    clicked.set('Select')
    listlabel = Label(buyframe, text="Choose share",
                      font="arial 15 bold", bg="black", fg="#228B22")
    listlabel.grid(row=11, column=1)
    dropdown = OptionMenu(buyframe, clicked, *options)
    dropdown.config(bg="green")
    dropdown.config(borderwidth=10)
    dropdown.config(relief="groove")
    dropdown.config(padx=100)
    dropdown.config(font="arial 10 bold")
    dropdown.grid(row=11, column=2, columnspan=4)
    if ordertype == "buy":
        buybutton = Button(buyframe, text="Confirm Order", relief="groove", activeforeground="pink", activebackground="white",
                           font="arial 10 bold", padx=20, pady=5, command=lambda: purchaseorder(quant.get(), clicked.get(), acc, passw, demat_number), fg="white", bg="#DC143C")
    else:
        buybutton = Button(buyframe, text="Confirm Order", relief="groove", activeforeground="pink", activebackground="white",
                           font="arial 10 bold", padx=20, pady=5, command=lambda: sellorder(quant.get(), clicked.get(), acc, passw, demat_number), fg="white", bg="#DC143C")
    buybutton.grid(row=13, column=2)


def adminlistofshares(acc, passw, querystring):
    try:
        ps_connection = psycopg2.connect(
            user=acc, password=passw, host="127.0.0.1", port="5432", database="stocksdb2")
        cursor = ps_connection.cursor()
        cursor.execute(querystring)

        result = cursor.fetchall()

        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")


def sellorder(quant, nse, acc, passw, dematno):
    date = dt.datetime.now()
    sell_date = f"{date:%Y-%m-%d}"
    availablelist = adminlistofshares(
        acc, passw, "select sum(number_of_shares), nse from a_shares group by nse;")
    for i in availablelist:
        if(i[1] == nse):
            availablequant = int(i[0])
    if int(quant) > int(availablequant):
        messagebox.showerror(
            title="Illegal Action", message=f"You have {availablequant} shares of {nse}. But you tried to sell {quant} shares.")
        return
    try:
        ps_connection = psycopg2.connect(
            user="postgres", password="vishnu2001", host="127.0.0.1", port="5432", database="stocksdb2")
        cursor = ps_connection.cursor()
        cursor.execute("select * from shares;")
        purprice = 0
        result = cursor.fetchall()
        for i in result:
            if i[0] == nse:
                purprice = float(i[1])

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")
    transid = adminaccessforbuy("select transactionid from transactions;")
    transid += 1
    fin1 = [transid, purprice, -1, quant, nse, dematno]
    totalprofitamount = float(purprice)*int(quant)
    try:
        ps_connection = psycopg2.connect(
            user=acc, password=passw, host="127.0.0.1", port="5432", database="stocksdb2")
        cursor = ps_connection.cursor()
        cursor.execute("select balance from account;")
        result = cursor.fetchall()
        cursor.execute(
            f"select price_at_buy , number_of_shares from a_shares where nse='{nse}'")
        restemp = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")
    investvalreturn = 0
    tottales = 0
    for i in restemp:
        tottales += i[0]
        investvalreturn += (i[0]*i[1])
    returnsval = (int(quant)*investvalreturn)/tottales
    querystring = "insert into transactions(transactionid, price_at_trans, sell_buy, shares_quant, stockid, demat_no)values(%s,%s,%s,%s,%s,%s);"
    insertin