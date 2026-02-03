import tkinter as tk

class Graphing():
    def __init__(self, master):
        self.master = master

    def show(self):
        self.label = tk.Label(self.master, text="Graph Screen")
        self.label.pack()