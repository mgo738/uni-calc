import tkinter as tk

class Tables():
    def __init__(self, master):
        self.master = master

    def show(self):
        self.label = tk.Label(self.master, text="Table Screen")
        self.label.pack()