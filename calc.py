import tkinter as tk
from PIL import Image, ImageTk

import calculate
import graphs
import table


class CalcMenu:
    def __init__(self):
        self.calc_image = Image.open("pictures/calculate-button.png")
        self.calc_image = self.calc_image.resize((400, 200))
        self.calc_button_image = ImageTk.PhotoImage(self.calc_image)

        self.graph_image = Image.open("pictures/graph-button.png")
        self.graph_image = self.graph_image.resize((400, 200))
        self.graph_button_image = ImageTk.PhotoImage(self.graph_image)

        self.table_image = Image.open("pictures/table-button.png")
        self.table_image = self.table_image.resize((400, 200))
        self.table_button_image = ImageTk.PhotoImage(self.table_image)

        self.calculator = calculate.Calculator(self.calc_window)
        self.graphing = graphs.Graphing(self.calc_window)
        self.tables = table.Tables(self.calc_window)


    def start(self):
        self.calc_window = tk.Tk()
        self.calc_window.title("Calculator Selection Menu")
        self.calc_window.geometry("500x800")
        self.calc_window.resizable(False, False)

        self.calc_window.update_idletasks()
        x = (self.calc_window.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.calc_window.winfo_screenheight() // 2) - (800 // 2)
        self.calc_window.geometry(f'+{x}+{y}')

        self.top_label = tk.Label(self.calc_window, text="Choose an option",
                                 font=("Georgia", 30, "bold"))
        self.top_label.pack(pady=10)

        self.calc_button = tk.Button(self.calc_window, image=self.calc_button_image, borderwidth=0,
                                    command=lambda: [self.calculator.show(), self.close_calc_menu()])
        self.graph_button = tk.Button(self.calc_window, image=self.graph_button_image, borderwidth=0,
                                     command=lambda: [self.graphing.show(), self.close_calc_menu()])
        self.table_button = tk.Button(self.calc_window, image=self.table_button_image, borderwidth=0,
                                     command=lambda: [self.tables.show(), self.close_calc_menu()])

        self.calc_button.pack(expand=True)
        self.graph_button.pack(expand=True)
        self.table_button.pack(expand=True)

        self.calc_window.mainloop()
    

    def close_calc_menu(self):
        self.calc_window.withdraw()


if __name__ == "__main__":
    calculator = CalcMenu()
    calculator.start()