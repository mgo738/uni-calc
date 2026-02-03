import tkinter as tk

class Calculator():
    def __init__(self, master):
        self.master = master

    def show(self):
        self.master.title("Calculator Screen")
        self.frame_bg = "#999999"

        self.text_frame = tk.Frame(self.master, width=500, height=280, bg="white",
                                   borderwidth=0, highlightthickness=0)
        self.button_frame = tk.Frame(self.master, width=500, height=450, bg=self.frame_bg,
                                     borderwidth=0, highlightthickness=0)

        self.calc_text_label = tk.Label(self.text_frame, text="Calculator Display",
                                       font=("Georgia", 24), bg="white")
        
        # Number buttons
        self.button_0 = tk.Button(self.button_frame, text="0", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_1 = tk.Button(self.button_frame, text="1", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_2 = tk.Button(self.button_frame, text="2", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_3 = tk.Button(self.button_frame, text="3", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_4 = tk.Button(self.button_frame, text="4", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_5 = tk.Button(self.button_frame, text="5", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_6 = tk.Button(self.button_frame, text="6", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_7 = tk.Button(self.button_frame, text="7", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_8 = tk.Button(self.button_frame, text="8", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_9 = tk.Button(self.button_frame, text="9", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)

        # Operator/other buttons
        self.button_plus = tk.Button(self.button_frame, text="+", font=("Georgia", 26), 
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_minus = tk.Button(self.button_frame, text="-", font=("Georgia", 26), 
                                      borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_multiply = tk.Button(self.button_frame, text="x", font=("Georgia", 26), 
                                         borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_divide = tk.Button(self.button_frame, text="÷", font=("Georgia", 26), 
                                       borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_equals = tk.Button(self.button_frame, text="=", font=("Georgia", 26), 
                                       borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_backspace = tk.Button(self.button_frame, text="⌫", font=("Georgia", 26), 
                                          borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_clear = tk.Button(self.button_frame, text="C", font=("Georgia", 26), 
                                      borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_more = tk.Button(self.button_frame, text="More", font=("Georgia", 26), 
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_plus_minus = tk.Button(self.button_frame, text="±", font=("Georgia", 26), 
                                           borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_decimal = tk.Button(self.button_frame, text=".", font=("Georgia", 26), 
                                        borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        
        # Stop the frames from shrinking to the size of children widgets.
        # This fixes issue with label not being packed/anchored properly.
        self.text_frame.grid_propagate(False)
        self.button_frame.grid_propagate(False)

        self.master.grid_rowconfigure(1, minsize=280)
        self.master.grid_rowconfigure(2, minsize=450)
        self.master.grid_columnconfigure(0, minsize=500)

        self.text_frame.grid(row=1, column=0, sticky="nsew")
        self.button_frame.grid(row=2, column=0, sticky="nsew")

        self.button_frame.grid_rowconfigure(0, minsize=90)
        self.button_frame.grid_rowconfigure(1, minsize=90)
        self.button_frame.grid_rowconfigure(2, minsize=90)
        self.button_frame.grid_rowconfigure(3, minsize=90)
        self.button_frame.grid_rowconfigure(4, minsize=90)
        self.button_frame.grid_columnconfigure(0, minsize=125)
        self.button_frame.grid_columnconfigure(1, minsize=125)
        self.button_frame.grid_columnconfigure(2, minsize=125)
        self.button_frame.grid_columnconfigure(3, minsize=125)

        self.button_more.grid(row=0, column=0, sticky="nsew")
        self.button_clear.grid(row=0, column=1, sticky="nsew")
        self.button_backspace.grid(row=0, column=2, sticky="nsew")
        self.button_divide.grid(row=0, column=3, sticky="nsew")
        self.button_7.grid(row=1, column=0, sticky="nsew")
        self.button_8.grid(row=1, column=1, sticky="nsew")
        self.button_9.grid(row=1, column=2, sticky="nsew")
        self.button_multiply.grid(row=1, column=3, sticky="nsew")
        self.button_4.grid(row=2, column=0, sticky="nsew")
        self.button_5.grid(row=2, column=1, sticky="nsew")
        self.button_6.grid(row=2, column=2, sticky="nsew")
        self.button_minus.grid(row=2, column=3, sticky="nsew")
        self.button_1.grid(row=3, column=0, sticky="nsew")
        self.button_2.grid(row=3, column=1, sticky="nsew")
        self.button_3.grid(row=3, column=2, sticky="nsew")
        self.button_plus.grid(row=3, column=3, sticky="nsew")
        self.button_plus_minus.grid(row=4, column=0, sticky="nsew")
        self.button_0.grid(row=4, column=1, sticky="nsew")
        self.button_decimal.grid(row=4, column=2, sticky="nsew")
        self.button_equals.grid(row=4, column=3, sticky="nsew")


        self.calc_text_label.pack(side="bottom", anchor="w", padx=26, pady=26)