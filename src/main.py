from tkinter import Tk
from ui import StockSimulator

if __name__ == '__main__':
    root = Tk()
    app = StockSimulator(root)
    root.mainloop()