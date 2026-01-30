import tkinter as tk


class MenuOptions:
    def __init__(self, master, calc):
        self.window = tk.Toplevel(master)
        self.window.geometry("500x800")
        self.window.resizable(False, False)
        self.window.withdraw()

        self.master = master
        self.calc = calc

    def calculator(self):
        self.calc.closeCalcMenu()
        self.window.title("Calculator")
        self.window.wm_deiconify()
    
    def graph(self):
        self.calc.closeCalcMenu()
        self.window.title("Graphing Tool")
        self.window.wm_deiconify()
    
    def table(self):
        self.calc.closeCalcMenu()
        self.window.title("Tables and Statistics")
        self.window.wm_deiconify()