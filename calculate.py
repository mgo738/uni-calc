import tkinter as tk

class Calculator():
    def __init__(self, master):
        self.master = master

    def show(self):
        self.window = tk.Toplevel(self.master)
        self.window.geometry("500x800")
        self.window.resizable(False, False)
        self.window.title("Calculator")

        self.window.protocol("WM_DELETE_WINDOW", self.master.destroy)

        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.window.winfo_screenheight() // 2) - (800 // 2)
        self.window.geometry(f'+{x}+{y}')