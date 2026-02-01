import tkinter as tk
from PIL import Image, ImageTk
import calculate, graphs, table

class calcMenu:
    def __init__(self):
        self.calcWindow = tk.Tk()
        self.calcWindow.title("Calculator Selection Menu")
        self.calcWindow.geometry("500x800")
        self.calcWindow.resizable(False, False)

        self.calcWindow.update_idletasks()
        x = (self.calcWindow.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.calcWindow.winfo_screenheight() // 2) - (800 // 2)
        self.calcWindow.geometry(f'+{x}+{y}')

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

        self.calculator = calculate.calculator(self.calcWindow)
        self.graphing = graphs.graphing(self.calcWindow)
        self.tables = table.tables(self.calcWindow)
        self.calcButton = tk.Button(self.calcWindow, image=self.calcButtonImage, borderwidth=0, command=lambda: [self.calculator.show(), self.closeCalcMenu()])
        self.graphButton = tk.Button(self.calcWindow, image=self.graphButtonImage, borderwidth=0, command=lambda: [self.graphing.show(), self.closeCalcMenu()])
        self.tableButton = tk.Button(self.calcWindow, image=self.tableButtonImage, borderwidth=0, command=lambda: [self.tables.show(), self.closeCalcMenu()])

        self.calcButton.pack(expand=True)
        self.graphButton.pack(expand=True)
        self.tableButton.pack(expand=True)

        self.calcWindow.mainloop()
    
    def closeCalcMenu(self):
        self.calcWindow.withdraw()

if __name__ == "__main__":
    calculator = calcMenu()