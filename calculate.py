import tkinter as tk

class Calculator():
    def __init__(self, master):
        self.master = master

    def show(self):
        self.master.title("Calculator Screen")
        self.text_frame = tk.Frame(self.master, width=500, height=280, bg="white",
                                   borderwidth=0, highlightthickness=0)
        self.button_frame = tk.Frame(self.master, width=500, height=450, bg="#999999",
                                     borderwidth=0, highlightthickness=0)

        self.calc_text_label = tk.Label(self.text_frame, text="Calculator Display",
                                       font=("Georgia", 24), bg="white")
        
        self.text_frame.grid_propagate(False)
        self.button_frame.grid_propagate(False)

        self.master.grid_rowconfigure(1, minsize=280)
        self.master.grid_rowconfigure(2, minsize=450)
        self.master.grid_columnconfigure(0, minsize=500)

        self.text_frame.grid(row=1, column=0, sticky="nsew")
        self.button_frame.grid(row=2, column=0, sticky="nsew")

        self.calc_text_label.pack(side="bottom", anchor="w", padx=20, pady=20)