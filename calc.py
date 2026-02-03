import tkinter as tk
from PIL import Image, ImageTk

import calculate
import graphs
import table


class CalcMenu:
    def __init__(self):
        self.calc_image = Image.open("pictures/calculate-button.png")
        self.calc_image = self.calc_image.resize((400, 200))
        

        self.graph_image = Image.open("pictures/graph-button.png")
        self.graph_image = self.graph_image.resize((400, 200))
        
        self.table_image = Image.open("pictures/table-button.png")
        self.table_image = self.table_image.resize((400, 200))


    def start(self):
        self.calc_window = tk.Tk()
        self.calc_window.title("Calculator Selection Menu")
        self.calc_window.geometry("500x800")
        self.calc_window.resizable(False, False)

        self.calc_window.update_idletasks()
        x = (self.calc_window.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.calc_window.winfo_screenheight() // 2) - (800 // 2)
        self.calc_window.geometry(f'+{x}+{y}')

        self.table_button_image = ImageTk.PhotoImage(self.table_image)
        self.graph_button_image = ImageTk.PhotoImage(self.graph_image)
        self.calc_button_image = ImageTk.PhotoImage(self.calc_image)

        self.top_label = tk.Label(self.calc_window, text="Choose an option",
                                 font=("Georgia", 30, "bold"))
        self.top_label.pack(pady=10)

        self.calc_button = tk.Button(self.calc_window, image=self.calc_button_image, borderwidth=0,
                                    command=lambda: [self.close_calc_menu(), self.button_commands("calculate")])
        self.graph_button = tk.Button(self.calc_window, image=self.graph_button_image, borderwidth=0,
                                     command=lambda: [self.close_calc_menu(), self.button_commands("graph")])
        self.table_button = tk.Button(self.calc_window, image=self.table_button_image, borderwidth=0,
                                     command=lambda: [self.close_calc_menu(), self.button_commands("table")])
        
        self.calc_button.pack(expand=True)
        self.graph_button.pack(expand=True)
        self.table_button.pack(expand=True)

        self.calc_window.mainloop()
    

    def close_calc_menu(self):
        self.calc_window.withdraw()


    def create_window(self):
        self.window = tk.Toplevel(self.calc_window)
        self.window.title("Calculator Selection Menu")
        self.window.geometry("500x800")
        self.window.resizable(False, False)

        self.window.protocol("WM_DELETE_WINDOW", self.calc_window.destroy)

        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.window.winfo_screenheight() // 2) - (800 // 2)
        self.window.geometry(f'+{x}+{y}')
    
    
    def button_commands(self, screen):
        self.create_window()
        self.calculator = calculate.Calculator(self.window)
        self.graphing = graphs.Graphing(self.window)
        self.tables = table.Tables(self.window)

        if screen == "calculate":
            self.calculator.show()
        elif screen == "graph":
            self.graphing.show()
        elif screen == "table":
            self.tables.show()


if __name__ == "__main__":
    calculator = CalcMenu()
    calculator.start()