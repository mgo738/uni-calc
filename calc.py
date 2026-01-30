import menu_options as menu
import tkinter as tk
from PIL import Image, ImageTk

class calcMenu:
    def __init__(self):
        self.calcWindow = tk.Tk()
        self.calcWindow.title("Calculator")
        self.calcWindow.geometry("500x800")
        self.calcWindow.resizable(False, False)

        self.topLabel = tk.Label(self.calcWindow, text="Choose an option", font=("Georgia", 30, "bold"))
        self.topLabel.pack(pady=10)

        self.calcImage = Image.open("pictures/calculate-button.png")
        self.calcImage = self.calcImage.resize((400, 200))
        self.calcButtonImage = ImageTk.PhotoImage(self.calcImage)

        self.graphImage = Image.open("pictures/graph-button.png")
        self.graphImage = self.graphImage.resize((400, 200))
        self.graphButtonImage = ImageTk.PhotoImage(self.graphImage)

        self.tableImage = Image.open("pictures/table-button.png")
        self.tableImage = self.tableImage.resize((400, 200))
        self.tableButtonImage = ImageTk.PhotoImage(self.tableImage)

        menu.menuOptions = menu.MenuOptions(self.calcWindow, self)
        self.calcButton = tk.Button(self.calcWindow, image=self.calcButtonImage, font=("Arial", 18), borderwidth=0, command=menu.menuOptions.calculator)
        self.graphButton = tk.Button(self.calcWindow, image=self.graphButtonImage, font=("Arial", 18), borderwidth=0, command=menu.menuOptions.graph)
        self.tableButton = tk.Button(self.calcWindow, image=self.tableButtonImage, font=("Arial", 18), borderwidth=0, command=menu.menuOptions.table)

        self.calcButton.pack(expand=True)
        self.graphButton.pack(expand=True)
        self.tableButton.pack(expand=True)

        self.calcWindow.mainloop()
    
    def closeCalcMenu(self):
        self.calcWindow.withdraw()

    def getCalcWindow(self):
        self.calcWindow.wm_deiconify()

if __name__ == "__main__":
    calculator = calcMenu()