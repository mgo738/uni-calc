import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import csv

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

        try:
            with open(self.user_file, 'r') as file:
                csvReader = csv.reader(file)
                rows = list(csvReader)

                if not rows:
                    messagebox.showwarning("Empty File", "The CSV you selected is empty!")

                vertical_scrollbar = ttk.Scrollbar(self.table_window, orient="vertical")
                horizontal_scrollbar = ttk.Scrollbar(self.table_window, orient="horizontal")
                
                self.table_tree = ttk.Treeview(self.table_window, height=20, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
                horizontal_scrollbar.config(command=self.table_tree.xview)
                vertical_scrollbar.config(command=self.table_tree.yview)

                self.table_tree.grid(row=0, column=0, sticky="nsew")
                vertical_scrollbar.grid(row=0, column=1, sticky="ns")
                horizontal_scrollbar.grid(row=1, column=0, sticky="ew")

                self.table_window.rowconfigure(0, weight=1)
                self.table_window.columnconfigure(0, weight=1)

                headers = rows[0]
                self.table_tree["columns"] = headers
                self.table_tree.column("#0", width=0, stretch=False)

                for header in headers:
                    self.table_tree.heading(header, text=header)
                    self.table_tree.column(header, width=100, anchor="center")

                for row in rows[1:]:
                    self.table_tree.insert("", "end", values=row)

                self.button_frame = tk.Frame(self.table_window, width = 800, height = 50, bg="#5eee5e")
                self.button_frame.pack_propagate(False)
                self.button_frame.grid(row=2, column=0, rowspan=2, sticky="nsew")

                self.mean_button = tk.Button(self.button_frame, text="Calculate mean values", 
                                             bg='white', borderwidth=0, font=("Georgia", 10, "bold"),
                                             command=self.calculate_mean)
                self.sd_button = tk.Button(self.button_frame, text="Calculate Standard Deviation", 
                                           bg='white', borderwidth=0, font=("Georgia", 10, "bold"),
                                           command=self.calculate_standard_deviation)

                self.mean_button.pack(side='left', padx=20)
                self.sd_button.pack(side='left')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file:\n{e}")
        
    
    def calculate_mean(self):
        pass


    def calculate_standard_deviation(self):
        pass