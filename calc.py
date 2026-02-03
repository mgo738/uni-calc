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

        self.home_image = Image.open("pictures/home-icon.png")
        self.home_image = self.home_image.resize((50, 50))


    def start(self):
        self.calc_window = tk.Tk()
        self.calc_window.title("Calculator Selection Menu")
        self.calc_window.geometry("500x800")
        self.calc_window.resizable(False, False)

        # Centering the window on the screen.
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
                                    command=lambda: self.button_commands("calculate"))
        self.graph_button = tk.Button(self.calc_window, image=self.graph_button_image, borderwidth=0,
                                     command=lambda: self.button_commands("graph"))
        self.table_button = tk.Button(self.calc_window, image=self.table_button_image, borderwidth=0,
                                     command=lambda: self.button_commands("table"))
        
        
        self.calc_button.pack(expand=True)
        self.graph_button.pack(expand=True)
        self.table_button.pack(expand=True)

        self.calc_window.mainloop()
    

    def create_window(self):
        self.window = tk.Toplevel(self.calc_window)
        self.window.title("Calculator Selection Menu")
        self.window.geometry("500x800")
        self.window.resizable(False, False)

        # Protocol for the newly opened window.
        # When user closes the window using the 'x' button on window, it goes back to the selection menu.
        self.window.protocol("WM_DELETE_WINDOW", self.go_home)

        # Center the window on the screen.
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.window.winfo_screenheight() // 2) - (800 // 2)
        self.window.geometry(f'+{x}+{y}')

        self.canvas_bg = "#aaaaaa"
        self.canvas = tk.Canvas(self.window, width=500, height=70, bg=self.canvas_bg,
                                borderwidth=0, highlightthickness=0)

        self.home_button_image = ImageTk.PhotoImage(self.home_image)
        self.home_button = tk.Button(self.window, image=self.home_button_image, borderwidth=0,
                                    command=self.go_home, background=self.canvas_bg, activebackground=self.canvas_bg)
        self.title_label = tk.Label(self.window, text="Title",
                                    font=("Georgia", 28, "bold"), bg=self.canvas_bg)
        
        self.home_button.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        self.canvas.grid(row=0, column=0, columnspan=4)
        self.title_label.place(relx=0.5, y=35, anchor="center")
    

    def button_commands(self, screen):
        self.calc_window.withdraw()

        self.create_window()
        self.calculator = calculate.Calculator(self.window)
        self.graphing = graphs.Graphing(self.window)
        self.tables = table.Tables(self.window)

        if screen == "calculate":
            self.title_label.config(text="Calculator")
            self.canvas_bg = "#ec5858"
            self.calculator.show()
        elif screen == "graph":
            self.title_label.config(text="Graphing Tool")
            self.canvas_bg = "#5898ec"
            self.graphing.show()
        elif screen == "table":
            self.title_label.config(text="Table and Statistics")
            self.canvas_bg = "#5eee5e"
            self.tables.show()
        
        self.canvas.config(bg=self.canvas_bg)
        self.home_button.config(bg=self.canvas_bg, activebackground=self.canvas_bg)
        self.title_label.config(bg=self.canvas_bg)

    
    def go_home(self):
        self.window.destroy()
        self.calc_window.wm_deiconify()


if __name__ == "__main__":
    calculator = CalcMenu()
    calculator.start()