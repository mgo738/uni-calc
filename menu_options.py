import tkinter as tk


class MenuOptions:
    def __init__(self, master, calc):
        self.window = tk.Toplevel(master)
        self.window.geometry("500x800")
        self.window.resizable(False, False)
        self.window.withdraw()
        self.window.protocol("WM_DELETE_WINDOW", self.on_close) # AI helped me implement this initially, as I had bugs related to this specific issue.

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

    def on_close(self): # Created with some help from AI, as mentioned previously, this gave me a bug that I struggled to fix.
        try:
            self.calc.calcWindow.destroy()
        except Exception:
            pass
        try:
            self.window.destroy()
        except Exception:
            pass