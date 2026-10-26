import pandas as pd
from pynse import Nse
from tkinter import *
import psycopg2
from tkinter import ttk
import time
import datetime as dt
from tkinter import messagebox

nse = Nse()

root = Tk()


def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()


def update_stock_prices():
    try:
        ps_connection = psycopg2.connect(
            user="postgres", password="vishnu2001", host="127.0.0.1", port="5432", database="stocksdb2")
        cursor = ps_connection.cursor()
        cursor.execute("select nse_symbol from shares;")
        result = cursor.fetchall()
        for i in result:
            temp = nse.get_quote(i[0])['lastPrice']
            cursor.execute(f"update shares set share_price={temp} where nse_symbol='{i[0]}'")
            ps_connection.commit()
            print(f"Updated {i[0]} to price {temp}")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if ps_connection:
            cursor.close()
            ps_connection.close()
            print("PostgreSQL connection is closed")


root.after(60000, update_stock_prices)  # Update stock prices every minute

root.mainloop()