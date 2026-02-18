import tkinter as tk

class Graphing():
    def __init__(self, master):
        self.master = master

    def show(self):
        self.master.title("Graphing tool")

        # 2 options - equations: y=x², and from data - pandas dataframes
        # Equations will allow for a few equations at once. They should be able to find intersection of lines (gradient?)
        # DataFrames - to be studied, hopefuly Line of Best Fit can be drawn? PMCC?
