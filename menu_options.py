import tkinter as tk
from PIL import Image, ImageTk


class MenuOptions:
    def __init__(self, master, calc):
        self.window = tk.Toplevel(master)
        self.window.geometry("500x800")
        self.window.resizable(False, False)
        self.window.withdraw()
        self.window.protocol("WM_DELETE_WINDOW", self.on_close) # AI helped me implement this initially, as I had bugs related to this specific issue.

        homeImage = Image.open("pictures/home-icon.jpg")
        homeImage = homeImage.resize((50, 50))
        self.homeButtonImage = ImageTk.PhotoImage(homeImage)

        homeButton = tk.Button(self.window, image=self.homeButtonImage, borderwidth=0, command=self.home)
        homeButton.pack(anchor="nw", pady=10, padx=10)

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

    def home(self):
        self.window.withdraw()
        self.calc.calcWindow.wm_deiconify()