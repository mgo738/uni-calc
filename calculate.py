import tkinter as tk

class Calculator():
    def __init__(self, master):
        self.master = master

    def show(self):
        self.label = tk.Label(self.master, text="Calculator Screen")
        self.label.pack()