import menu_options as menu
import tkinter as tk
from PIL import Image, ImageTk

class calcMenu:
    def __init__(self):
        self.calcWindow = tk.Tk()
        self.calcWindow.title("Calculator")
        self.calcWindow.geometry("500x800")
        self.calcWindow.resizable(False, False)

        topLabel = tk.Label(self.calcWindow, text="Choose an option", font=("Georgia", 30, "bold"))
        topLabel.pack(pady=10)

        calcImage = Image.open("pictures/calculate-button.png")
        calcImage = calcImage.resize((400, 200))
        calcButtonImage = ImageTk.PhotoImage(calcImage)

        graphImage = Image.open("pictures/graph-button.png")
        graphImage = graphImage.resize((400, 200))
        graphButtonImage = ImageTk.PhotoImage(graphImage)

        tableImage = Image.open("pictures/table-button.png")
        tableImage = tableImage.resize((400, 200))
        tableButtonImage = ImageTk.PhotoImage(tableImage)

        calcButton = tk.Button(self.calcWindow, image=calcButtonImage, font=("Arial", 18), borderwidth=0)
        graphButton = tk.Button(self.calcWindow, image=graphButtonImage, font=("Arial", 18), borderwidth=0)
        tableButton = tk.Button(self.calcWindow, image=tableButtonImage, font=("Arial", 18), borderwidth=0)

        calcButton.pack(expand=True)
        graphButton.pack(expand=True)
        tableButton.pack(expand=True)

        self.calcWindow.mainloop()
    
    def closeCalcMenu(self):
        self.calcWindow.withdraw()

    def getCalcWindow(self):
        self.calcWindow.wm_deiconify()

calculator = calcMenu()