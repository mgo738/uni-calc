import menu_options as menu
import tkinter as tk
from PIL import Image, ImageTk

calcWindow = tk.Tk()
calcWindow.title("Calculator")
calcWindow.geometry("500x800")
calcWindow.resizable(False, False)

topLabel = tk.Label(calcWindow, text="Choose an option", font=("Georgia", 30, "bold"))
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

calcButton = tk.Button(calcWindow, image=calcButtonImage, font=("Arial", 18), borderwidth=0)
graphButton = tk.Button(calcWindow, image=graphButtonImage, font=("Arial", 18), borderwidth=0)
tableButton = tk.Button(calcWindow, image=tableButtonImage, font=("Arial", 18), borderwidth=0)

calcButton.pack(expand=True)
graphButton.pack(expand=True)
tableButton.pack(expand=True)

calcWindow.mainloop()