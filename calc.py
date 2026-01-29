import menu_options as menu
import tkinter as tk

calcWindow = tk.Tk()
calcWindow.title("Calculator")
calcWindow.geometry("500x800")

topLabel = tk.Label(calcWindow, text="Choose an option", font=("Arial", 24, "bold"))
topLabel.pack(pady=10)

calcButton = tk.Button(calcWindow, text="Calculator", font=("Arial", 18), width=20, height=3)
graphButton = tk.Button(calcWindow, text="Graph", font=("Arial", 18), width=20, height=3)
tableButton = tk.Button(calcWindow, text="Table", font=("Arial", 18), width=20, height=3)

calcButton.pack(expand=True)
graphButton.pack(expand=True)
tableButton.pack(expand=True)

calcWindow.mainloop()