import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import pandas as pd
import math

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
                csvReader = pd.read_csv(file)
                csvReader = csvReader.dropna()

                head_values = csvReader.columns.tolist()
                rows = [head_values] + csvReader.values.tolist()

                if not rows:
                    messagebox.showwarning("Empty File", "The CSV you selected is empty!")

                vertical_scrollbar = ttk.Scrollbar(self.table_window, orient="vertical")
                horizontal_scrollbar = ttk.Scrollbar(self.table_window, orient="horizontal")
                
                self.table_tree = ttk.Treeview(self.table_window, height=20, xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)
                horizontal_scrollbar.config(command=self.table_tree.xview)
                vertical_scrollbar.config(command=self.table_tree.yview)
                self.table_tree.bind("<Double-1>", self.on_double_click)

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
                                             command=self.create_mean_window)
                self.sd_button = tk.Button(self.button_frame, text="Calculate Standard Deviation", 
                                           bg='white', borderwidth=0, font=("Georgia", 10, "bold"),
                                           command=self.create_standard_window)
                self.export_button = tk.Button(self.button_frame, text="Export File", 
                                           bg='white', borderwidth=0, font=("Georgia", 10, "bold"),
                                           command=self.export_file)
                self.save_button = tk.Button(self.button_frame, text="Save File", 
                                           bg='white', borderwidth=0, font=("Georgia", 10, "bold"),
                                           command=self.save_file)

                self.mean_button.pack(side='left', padx=20)
                self.sd_button.pack(side='left')
                self.export_button.pack(side='right',padx=20)
                self.save_button.pack(side='right')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file:\n{e}")
        
    
    def calculate_mean(self):
        self.mean_headers = []
        self.totals_to_insert = []
        self.counts_to_insert = []
        self.means_to_insert = []
        for column_id, column_name in enumerate(self.table_tree["columns"]):
            total = 0
            count = 0
            try:
                for item in self.table_tree.get_children():
                    total += float(self.table_tree.item(item)["values"][column_id])
                    count += 1
                
                self.mean_headers.insert(column_id, column_name)
                self.totals_to_insert.insert(column_id, total)
                self.counts_to_insert.insert(column_id, count)
                self.means_to_insert.insert(column_id, round(total/count, 2))
            except Exception:
                self.mean_headers.insert(column_id, column_name)
                self.totals_to_insert.insert(column_id, "N/A")
                self.counts_to_insert.insert(column_id, "N/A")
                self.means_to_insert.insert(column_id, "N/A")


    def calculate_standard_deviation(self):
        self.calculate_mean()

        self.sd_headers = []
        self.square_means_to_insert = []
        self.standard_devs_to_insert = []
        for column_id, column_name in enumerate(self.table_tree["columns"]):
            total = 0
            count = 0
            try:
                for item in self.table_tree.get_children():
                    total += float(self.table_tree.item(item)["values"][column_id])
                    count += 1
                
                self.sd_headers.insert(column_id, column_name)
                self.square_means_to_insert.insert(column_id, round((total**2)/count, 2))
                self.standard_devs_to_insert.insert(column_id, round(math.sqrt(self.square_means_to_insert[column_id] - (self.means_to_insert[column_id]**2)), 2))
            except Exception:
                self.sd_headers.insert(column_id, column_name)
                self.square_means_to_insert.insert(column_id, "N/A")
                self.standard_devs_to_insert.insert(column_id, "N/A")


    def create_mean_window(self):
        self.calculate_mean()

        self.mean_window = tk.Toplevel(self.table_window)
        self.mean_window.geometry("500x300")
        self.mean_window.title("Mean values")

        self.mean_horizontal_scrollbar = ttk.Scrollbar(self.mean_window, orient="horizontal")

        self.mean_tree = ttk.Treeview(self.mean_window, xscrollcommand=self.mean_horizontal_scrollbar.set)
        self.mean_horizontal_scrollbar.config(command=self.mean_tree.xview)
        self.mean_tree.column('#0', width=80, stretch=False)

        self.mean_tree.grid(row=0, column=0, sticky='nsew')
        self.mean_horizontal_scrollbar.grid(row=1, column=0, sticky='ew')

        self.mean_window.rowconfigure(0, weight=1)
        self.mean_window.columnconfigure(0, weight=1)

        self.mean_tree["columns"] = self.mean_headers
        for header in self.mean_headers:
            self.mean_tree.heading(header, text=header)
            self.mean_tree.column(header, width=100, anchor='center')

        self.mean_tree.insert("", "end", text="Total (Σx):", values=self.totals_to_insert)
        self.mean_tree.insert("", "end", text="Count (n):", values=self.counts_to_insert)
        self.mean_tree.insert("", "end", text="Mean (x̄):", values=self.means_to_insert)
    

    def create_standard_window(self):
        self.calculate_standard_deviation()

        self.sd_window = tk.Toplevel(self.table_window)
        self.sd_window.geometry("600x350")
        self.sd_window.title("Mean values")

        self.sd_horizontal_scrollbar = ttk.Scrollbar(self.sd_window, orient="horizontal")

        self.sd_tree = ttk.Treeview(self.sd_window, xscrollcommand=self.sd_horizontal_scrollbar.set)
        self.sd_horizontal_scrollbar.config(command=self.sd_tree.xview)
        self.sd_tree.column('#0', width=140, stretch=False)

        self.sd_tree.grid(row=0, column=0, sticky='nsew')
        self.sd_horizontal_scrollbar.grid(row=1, column=0, sticky='ew')

        self.sd_window.rowconfigure(0, weight=1)
        self.sd_window.columnconfigure(0, weight=1)

        self.sd_tree["columns"] = self.sd_headers
        for header in self.sd_headers:
            self.sd_tree.heading(header, text=header)
            self.sd_tree.column(header, width=100, anchor='center')

        self.sd_tree.insert("", "end", text="Total (Σx):", values=self.totals_to_insert)
        self.sd_tree.insert("", "end", text="Count (n):", values=self.counts_to_insert)
        self.sd_tree.insert("", "end", text="Mean (x̄):", values=self.means_to_insert)
        self.sd_tree.insert("", "end", text="Sum of Squares (Σx²):", values=self.square_means_to_insert)
        self.sd_tree.insert("", "end", text="Standard Deviation (σ):", values=self.standard_devs_to_insert)

    
    def save_changes(self):
        value_to_change = self.value_editor.get()
        row_values = list(self.table_tree.item(self.click_row, "values"))
        row_values[self.click_column] = value_to_change

        self.table_tree.item(self.click_row, values=row_values)
        self.value_editor.destroy()


    def cancel_changes(self):
        self.value_editor.destroy()
    
    
    def on_double_click(self, event):
        click_region = self.table_tree.identify_region(event.x, event.y)

        if click_region != "cell":
            return
        
        self.click_row = self.table_tree.identify_row(event.y)
        self.click_column = self.table_tree.identify_column(event.x)
        x_position, y_position, entry_width, entry_height = self.table_tree.bbox(self.click_row, self.click_column)

        if not self.click_row or not self.click_column:
            return
        
        self.click_column = int(self.click_column.replace("#", "")) - 1
        current_value = self.table_tree.item(self.click_row, "values")[self.click_column]

        self.value_editor = tk.Entry(self.table_window, justify='center')
        self.value_editor.place(x=x_position, y=y_position, width=entry_width, height=entry_height)
        self.value_editor.insert(0, current_value)
        self.value_editor.focus()

        self.value_editor.bind("<Return>", lambda e: self.save_changes())
        self.value_editor.bind("<FocusOut>", lambda e: self.save_changes())
        self.value_editor.bind("<Escape>", lambda e: self.cancel_changes())


    def export_file(self):
        print("File Exported!")


    def save_file(self):
        print("File Saved!")