import tkinter as tk
from tkinter import filedialog
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

        self.title_label = tk.Label(self.entry_frame, text="Enter full file path:", font=("Georgia", 24, "bold"))
        self.title_label.pack(anchor='n', pady=50)

        self.file_entry = tk.Entry(self.entry_frame, width=40)
        self.file_entry.bind("<Return>", lambda e: self.use_file("use"))
        self.file_entry.pack(anchor='n')

        self.use_button = tk.Button(self.entry_frame, width=10, height=1, bg='white', 
                                      borderwidth=0, text='Use file', font=("Georgia", 14),
                                      command=lambda: self.use_file("use"))
        self.use_button.pack(anchor='n', pady=20)

        self.open_button = tk.Button(self.entry_frame, width=10, height=1, bg='white', 
                                      borderwidth=0, text='Open file', font=("Georgia", 14),
                                      command=lambda: self.use_file("open"))
        self.open_button.pack(anchor='n')

        self.error_label = tk.Label(self.entry_frame, font=("Georgia", 18, "bold"), fg="#B10A0A", text="")
        self.error_label.pack(anchor='n', pady=20)
    

    def use_file(self, use):
        if use == "use":
            self.user_file = self.file_entry.get().strip()
        elif use == "open":
            self.user_file = filedialog.askopenfilename(
                title="Select CSV File",
                filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
            )

        if not os.path.isfile(self.user_file):
            self.error_label.config(text="Error: File does not exist.")
            return None
        
        if not self.user_file.endswith(".csv"):
            self.error_label.config(text="Error: File type must be .csv only")
            return None

        self.show_table()
    

    def show_table(self):
        self.table_window = tk.Toplevel(self.master)
        self.table_window.geometry("800x500")
        self.table_window.title("Table")