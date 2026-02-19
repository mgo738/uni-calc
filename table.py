import tkinter as tk
import os

class Tables():
    def __init__(self, master):
        self.master = master
        self.user_file = ""

    def show(self):
        self.master.title("Table and Statistics")

        # Import a CSV file which will be read from to create table
        # Once table created, user can find mean, variance, standard deviation etc...
        self.entry_frame = tk.Frame(self.master, width=500, height=730)
        self.entry_frame.pack_propagate(False)
        self.entry_frame.grid()

        self.title_label = tk.Label(self.entry_frame, text="Input file name:", font=("Georgia", 24, "bold"))
        self.title_label.pack(anchor='n', pady=50)

        self.file_entry = tk.Entry(self.entry_frame, width=40)
        self.file_entry.bind("<Return>", lambda e: self.show_table())
        self.file_entry.pack(anchor='n')

        self.entry_button = tk.Button(self.entry_frame, width=10, height=1, bg='white', 
                                      borderwidth=0, text='Open file', font=("Georgia", 14),
                                      command=self.show_table)
        self.entry_button.pack(anchor='n', pady=20)

        self.error_label = tk.Label(self.entry_frame, font=("Georgia", 20, "bold"), fg="#B10A0A", text="")
        self.error_label.pack(anchor='n', pady=10)
    
    def show_table(self):
        self.user_file = self.file_entry.get().strip()

        if not os.path.isfile(self.user_file):
            self.error_label.config(text="Error: File does not exist.")
            return None
        
        if not self.user_file.endswith(".csv"):
            self.error_label.config(text="Error: File type must be .csv only")
            return None
