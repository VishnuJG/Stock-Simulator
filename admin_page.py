from tkinter import *
import psycopg2
from tkinter import ttk

root = Tk()
root.title('Admin Page')

def view_transactions():
    try:
        ps_connection = psycopg2.connect(
            user='postgres', password='yourpassword', host='127.0.0.1', port='5432', database='stocksdb2')
        cursor = ps_connection.cursor()
        cursor.execute('SELECT * FROM transactions;')
        records = cursor.fetchall()
        for index, record in enumerate(records):
            for j, value in enumerate(record):
                transaction_table.set(index, j, value)
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error while connecting to PostgreSQL', error)
    finally:
        if ps_connection:
            cursor.close()
            ps_connection.close()

def view_shares():
    try:
        ps_connection = psycopg2.connect(
            user='postgres', password='yourpassword', host='127.0.0.1', port='5432', database='stocksdb2')
        cursor = ps_connection.cursor()
        cursor.execute('SELECT * FROM shares;')
        records = cursor.fetchall()
        for index, record in enumerate(records):
            for j, value in enumerate(record):
                shares_table.set(index, j, value)
    except (Exception, psycopg2.DatabaseError) as error:
        print('Error while connecting to PostgreSQL', error)
    finally:
        if ps_connection:
            cursor.close()
            ps_connection.close()

# Create buttons for viewing transactions and shares
Button(root, text='View Transactions', command=view_transactions).pack(pady=10)
Button(root, text='View Shares', command=view_shares).pack(pady=10)

# Create Treeview for displaying transactions
transaction_table = ttk.Treeview(root, columns=('ID', 'Price', 'Type', 'Quantity', 'Stock ID', 'Demat No'), show='headings')
transaction_table.pack()
for col in transaction_table['columns']:
    transaction_table.heading(col, text=col)

# Create Treeview for displaying shares
shares_table = ttk.Treeview(root, columns=('NSE Symbol', 'Share Price', 'Quantity'), show='headings')
shares_table.pack()
for col in shares_table['columns']:
    shares_table.heading(col, text=col)

root.mainloop()