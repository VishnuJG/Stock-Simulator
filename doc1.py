from tkinter import *
import psycopg2
from tkinter import ttk
root = Tk()


def clear_frame():
    for widgets in outtabledisplay.winfo_children():
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

spacer1 = Label(loginframe, text="", bg="black")
spacer1.grid(row=2, column=0)

labelpass = Label(loginframe, text="Enter your password",
                  font="arial 10 bold", bg="black", fg="#228B22")
labelpass.grid(row=3, column=0)

passw = Entry(loginframe, show="*", width=50, bg="#228B22", fg="yellow",
              borderwidth=10, font="arial 10 bold", textvariable=var2)
passw.grid(row=3, column=1)
passw.insert(0, "")

spacer2 = Label(loginframe, text="", bg="black")
spacer2.grid(row=4, column=0)


def myfun():
    inp = var1.get()
    inppass = var2.get()
    # print(inp,inppass)
    loginframe.pack_forget()
    controlroom(inp, inppass)


acc = ""
displaytable = LabelFrame(loginframe, text="test", bg="black",
                          fg="white", padx=10, pady=10).grid(row=0,column=1)
submitbutton = Button(loginframe, text="Submit", relief="groove", activeforeground="pink", activebackground="white",
                      font="arial 10 bold", padx=20, pady=5, command=myfun, fg="white", bg="#228B22").grid(row=5, column=1)


def controlroom(acc, passw):
    framehome = LabelFrame(root, text="Welcome", bg="black",
                           fg="white", padx=10, pady=10).pack()
    transactions_button = Button(framehome, text="Transaction details", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                                 padx=150, pady=5, command=lambda: afterlogin(f"select * from transactions ;", "transactions", acc, passw), fg="white", bg="#228B22")
    transactions_button.pack()
    a_shares_button = Button(framehome, text="Account shares details", relief="groove", activeforeground="pink", activebackground="white",
                             font="arial 10 bold", padx=100, pady=5, command=lambda: afterlogin(f"select * from a_shares ;", "a_shares", acc, passw), fg="white", bg="#228B22")
    a_shares_button.pack()
    company_button = Button(framehome, text="List Companies", relief="groove", activeforeground="pink", activebackground="white", font="arial 10 bold",
                            padx=100, pady=5, command=lambda: afterlogin(f"select * from company ;", "company", acc, passw), fg="white", bg="#228B22")
    company_button.pack()


def afterlogin(querystring, tablename, acc, passw):
    try:
        ps_connection = psycopg2.connect(
            user=acc, password=passw, host="127.0.0.1", port="5432", database="stocksdb2")
        cursor = ps_connection.cursor()
        cursor.execute(querystring)
        colnames = [desc[0] for desc in cursor.description]
        # tempres=""
        print(f"Fetching {tablename} details")
        result = cursor.fetchall()
        for i in range(len(result)):
            for j in range(len(colnames)):
                print(colnames[j]+'='+str(result[i][j]), end=" ")

            print("\n")

        outtabledisplay(colnames, result, tablename)

        return result

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # closing database connection.
        if ps_connection:
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")


def outtabledisplay(colnames, result, tablename):
    # clear_frame()
    global displaytable
    displaytable.pack_forget()
    displaytable = LabelFrame(root, text=tablename,
                              bg="black", fg="white", padx=10, pady=10).pack()
    outtable = ttk.Treeview(displaytable)
    outtable['columns'] = colnames
    outtable.column("#0", width=0,  stretch=NO)
    for j in range(len(colnames)):
        outtable.column(colnames[j], anchor=CENTER, width=80)
    outtable.heading("#0", text="", anchor=CENTER)
    for j in range(len(colnames)):
        outtable.heading(colnames[j], text=colnames[j], anchor=CENTER)

    for i in range(len(result)):
        outtable.insert(parent='', index='end', iid=i,
                        text='', values=result[i])
        outtable.pack()


root.mainloop()
