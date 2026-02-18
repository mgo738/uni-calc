import tkinter as tk

class Tables():
    def __init__(self, master):
        self.master = master

    def show(self):
        self.master.title("Table and Statistics")

        # Import a CSV file which will be read from to create table
        # Once table created, user can find mean, variance, standard deviation etc...
