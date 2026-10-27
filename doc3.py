import pandas as pd
from pynse import *
from tkinter import *
import psycopg2
from tkinter import ttk
import time
import datetime as dt
from tkinter import messagebox
from psycopg2 import sql

root = Tk()
root["bg"] = "black"
root.title('Login')
root["padx"] = 50
root["pady"] = 50


def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()


def myfun(inp, inppass):
    try:
        ps_connection = psycopg2.connect(
            user=inp, password=inppass, host="127.0.0.1", port="5432", database="stocksdb2")
        cursor = ps_connection.cursor()
        cursor.execute("SELECT * FROM account;")
        demat_number = StringVar()
        result = cursor.fetchall()
        demat_number = result[0][0]
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
        messagebox.showerror(title="Error", message=error)
    finally:
        if ps_connection:
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")
    clear_frame()
    controlroom(inp, inppass, demat_number)


def newaccfuntoupdate(c_name, pan, age, emailidno, passw):
    try:
        ps_connection = psycopg2.connect(
            user="postgres", password="vishnu2001", host="127.0.0.1", port="5432", database="stocksdb2")
        cursor = ps_connection.cursor()
        cursor.execute("SELECT demat_no FROM account;")
        result = cursor.fetchall()
        result.sort()
        dem = int(result[-1][0]) + 1
        cursor.execute(
            f"INSERT INTO account(demat_no, profit, invested, currentval, balance) VALUES({dem}, 0.0, 0.0, 0.0, 0.0);")
        ps_connection.commit()
        cursor.execute(
            f"INSERT INTO client(pan, c_name, age, emailid, demat_no) VALUES('{pan}', '{c_name}', {age}, '{emailidno}', {dem});")
        ps_connection.commit()
        query = sql.SQL("CREATE USER {0} WITH PASSWORD {1};").format(
            sql.Identifier(emailidno),
            sql.Literal(passw),)
        cursor.execute(query)
        ps_connection.commit()
        cursor.execute(f"GRANT clients TO \"{emailidno}\";")
        ps_connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
        messagebox.showerror(title="Failed", message=error)
    finally:
        if ps_connection:
            cursor.close()
            ps_connection.close()
        messagebox.showinfo(
            title="Success", message="Account creation Successful!!")
        loginfirst()


def newaccount():
    clear_frame()
    welcomelabel = Label(root, text="New Account", font="arial 20 bold",
                         bg="black", fg="#ffffff")
    welcomelabel.grid(row=0, column=1)
    clabel = Label(root, text="Enter your full name ",
                   font="arial 10 bold", bg="black", fg="#228B22")
    clabel.grid(row=1, column=0)
    c_name = Entry(root, width=50, bg="#228B22", fg="yellow",
                   borderwidth=10, font="arial 10 bold")
    c_name.grid(row=1, column=1)
    panlabel = Label(root, text="Enter your PAN number ",
                     font="arial 10 bold", bg="black", fg="#228B22")
    panlabel.grid(row=2, column=0)
    panent = Entry(root, width=50, bg="#228B22", fg="yellow",
                   borderwidth=10, font="arial 10 bold")
    panent.grid(row=2, column=1)
    agelabel = Label(root, text="Enter your age ",
                     font="arial 10 bold", bg="black", fg="#228B22")
    agelabel.grid(row=3, column=0)
    ageent = Entry(root, width=50, bg="#228B22", fg="yellow",
                   borderwidth=10, font="arial 10 bold")
    ageent.grid(row=3, column=1)
    emaillabel = Label(root, text="Enter your email id ",
                       font="arial 10 bold", bg="black", fg="#228B22")
    emaillabel.grid(row=4, column=0)
    emailent = Entry(root, width=50, bg="#228B22", fg="yellow",
                     borderwidth=10, font="arial 10 bold")
    emailent.grid(row=4, column=1)
    passwnewlabel = Label(root, text="Enter password",
                          font="arial 10 bold", bg="black", fg="#228B22")
    passwnewlabel.grid(row=5, column=0)
    passwnew = Entry(root, width=50, bg="#228B22", fg="yellow",
                     borderwidth=10, font="arial 10 bold")
    passwnew.grid(row=5, column=1)
    submitnewaccount = Button(root, text="Submit", relief="groove", activeforeground="pink", activebackground="white",
                              font="arial 10 bold", padx=20, pady=5, command=lambda: newaccfuntoupdate(c_name.get(), panent.get(), ageent.get(), emailent.get(), passwnew.get()), fg="white", bg="#228B22", borderwidth=8)
    submitnewaccount.grid(row=6, column=1)


def clearanceroom():
    root.destroy()


def loginfirst():
    clear_frame()
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
    passw = Entry(root, show="*", width=50, bg="#228B22", fg="yellow",
                  borderwidth=10, font="arial 10 bold", textvariable=var2)
    passw.grid(row=3, column=1)
    submitbutton = Button(root, text="Submit", relief="groove", activeforeground="pink", activebackground="white",
                          font="arial 10 bold", padx=20, pady=5, command=lambda: myfun(emailid.get(), passw.get()), fg="white", bg="#228B22", borderwidth=8).grid(row=5, column=1)
    companylogin = Button(root, text="Exit", relief="groove", activeforeground="pink", activebackground="white",
                          font="arial 10 bold", padx=20, pady=5, command=clearanceroom, fg="white", bg="#ffbf00", borderwidth=8).grid(row=6, column=2)
    createnewaccount = Button(root, text="Create account", relief="groove", activeforeground="pink", activebackground="white",
                              font="arial 10 bold", padx=20, pady=5, command=newaccount, fg="white", bg="#228B22", borderwidth=8).grid(row=6, column=0)


loginfirst()  # STARTS here


def controlroom(acc, passw, demat_number):
    homelabel = Label(root, text=f"Welcome {acc}", font="arial 25 bold",
                      bg="black", fg="white", padx=25, pady=20)
    homelabel.grid(row=0, column=1, columnspan=9)
    framehome = LabelFrame(root, text="Welcome", bg="black",
                           fg="white", padx=10, pady=10).grid(row=1, column=1)
    transactions_button = Button(framehome, text="Transaction details", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                                 padx=161, pady=5, command=lambda: afterlogin(f"SELECT * FROM transactions;", "transactions", acc, passw), fg="white", bg="#228B22")
    transactions_button.grid(row=1, column=1)
    a_shares_button = Button(framehome, text="Holdings", relief="groove", activeforeground="pink", activebackground="white",
                             font="arial 10 bold", padx=193, pady=5, command=lambda: afterlogin(f"SELECT nse, SUM(number_of_shares) AS Quantity, share_price AS LTP FROM a_shares, shares WHERE nse_symbol=nse GROUP BY nse, share_price;", "a_shares", acc, passw), fg="white", bg="#228B22")
    a_shares_button.grid(row=2, column=1)
    spacer3 = Label(root, text="", bg="black", padx=10)
    spacer3.grid(row=1, column=2)
    spacer4 = Label(root, text="", bg="black", padx=10)
    spacer4.grid(row=2, column=2)
    company_button = Button(framehome, text="List Companies", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                            padx=153, pady=5, command=lambda: afterlogin(f"SELECT * FROM company;", "company", acc, passw), fg="white", bg="#228B22")
    company_button.grid(row=1, column=3)
    view_shares_button = Button(framehome, text="List Shares", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                                padx=166, pady=5, command=lambda: afterlogin(f"SELECT * FROM shares;", "shares", acc, passw), fg="white", bg="#228B22")
    view_shares_button.grid(row=2, column=3)
    viewevents = Button(framehome, text="Events", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                        padx=181, pady=5, command=lambda: afterlogin(f"SELECT * FROM events;", "companies", acc, passw), fg="white", bg="#228B22")
    viewevents.grid(row=3, column=3)
    buybutton = Button(framehome, text="Buy Shares", relief="groove", activeforeground="green", activebackground="black", font="arial 10 bold",
                       padx=185, pady=5, command=lambda: buyphase(acc, passw, demat_number, 'buy'), fg="white", bg="#DC143C")
    buybutton.grid(row=4, column=1)
    accountdetails = Button(framehome, text="Account details", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                            padx=172, pady=5, command=lambda: afterlogin(f"SELECT * FROM account;", "account", acc, passw), fg="white", bg="#228B22")
    accountdetails.grid(row=3, column=1)
    sell_button = Button(framehome, text="Sell shares", relief="groove", activeforeground="green", activebackground="black", font="arial 10 bold",
                         padx=168, pady=5, command=lambda: buyphase(acc, passw, demat_number, 'sell'), fg="white", bg="#DC143C")
    sell_button.grid(row=4, column=3)
    varn = 0.0
    balanceenter = Entry(framehome, width=10, bg="#228B22", fg="yellow",
                         borderwidth=10, font="arial 10 bold", textvariable=varn)
    balanceenter.grid(row=5, column=2)
    balanceinput = Button(framehome, text="Add amount to wallet", relief="groove", activeforeground="green", activebackground="black", font="arial 10 bold",
                          padx=154, pady=5, command=lambda: updatebalance(balanceenter.get(), acc, passw, 1), fg="white", bg="#0099CC")
    balanceinput.grid(row=5, column=1)
    balancewithn = Entry(framehome, width=10, bg="#228B22", fg="yellow",
                         borderwidth=10, font="arial 10 bold")
    balancewithn.grid(row=6, column=2)
    balancewith = Button(framehome, text="Withdraw amount from wallet", relief="groove", activeforeground="green", activebackground="black", font="arial 10 bold",
                         padx=128, pady=5, command=lambda: updatebalance(balancewithn.get(), acc, passw, 0), fg="white", bg="#0099CC")
    balancewith.grid(row=6, column=1)



def updatebalance(balamt, acc, passw, addorsub):
    try:
        ps_connection = psycopg2.connect(
            user=acc, password=passw, host="127.0.0.1", port="5432", database="stocksdb2")
        cursor = ps_connection.cursor()
        if addorsub == 1:
            cursor.execute(f"UPDATE account SET balance=balance+{balamt};")
        else:
            cursor.execute(f"UPDATE account SET balance=balance-{balamt};")
        ps_connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if ps_connection:
            cursor.close()
            ps_connection.close()
