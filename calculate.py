import tkinter as tk

class Calculator():
    def __init__(self, master):
        self.master = master
        self.last_pressed_equals = False
        self.numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        self.operators = ["+", "-", "x", "÷"]

    def show(self):
        self.master.title("Calculator Screen")
        self.frame_bg = "#aaaaaa"

        self.text_frame = tk.Frame(self.master, width=500, height=280, bg="white",
                                   borderwidth=0, highlightthickness=0)
        self.button_frame = tk.Frame(self.master, width=500, height=450, bg=self.frame_bg,
                                     borderwidth=0, highlightthickness=0)
        self.more_button_frame = tk.Frame(self.master, width=500, height=450, bg=self.frame_bg,
                                         borderwidth=0, highlightthickness=0)

        self.calc_text_label = tk.Label(self.text_frame, text="",
                                       font=("Georgia", 24), bg="white")
        self.answer_text_label = tk.Label(self.text_frame, text="",
                                         font=("Georgia", 24), bg="white")
        self.previous_text_label = tk.Label(self.text_frame, text="",
                                           font=("Georgia", 18), bg="white", fg="#555555")
        
        # Number buttons
        self.button_0 = tk.Button(self.button_frame, text="0", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                  command=lambda: self.button_functions(self.button_0))
        self.button_1 = tk.Button(self.button_frame, text="1", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                  command=lambda: self.button_functions(self.button_1))
        self.button_2 = tk.Button(self.button_frame, text="2", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                  command=lambda: self.button_functions(self.button_2))
        self.button_3 = tk.Button(self.button_frame, text="3", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                  command=lambda: self.button_functions(self.button_3))
        self.button_4 = tk.Button(self.button_frame, text="4", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                  command=lambda: self.button_functions(self.button_4))
        self.button_5 = tk.Button(self.button_frame, text="5", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                  command=lambda: self.button_functions(self.button_5))
        self.button_6 = tk.Button(self.button_frame, text="6", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                  command=lambda: self.button_functions(self.button_6))
        self.button_7 = tk.Button(self.button_frame, text="7", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                  command=lambda: self.button_functions(self.button_7))
        self.button_8 = tk.Button(self.button_frame, text="8", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                  command=lambda: self.button_functions(self.button_8))
        self.button_9 = tk.Button(self.button_frame, text="9", font=("Georgia", 26), 
                                  borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                  command=lambda: self.button_functions(self.button_9))

        # Operator/other buttons
        self.button_plus = tk.Button(self.button_frame, text="+", font=("Georgia", 26), 
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                     command=lambda: self.button_functions(self.button_plus))
        self.button_minus = tk.Button(self.button_frame, text="-", font=("Georgia", 26), 
                                      borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                      command=lambda: self.button_functions(self.button_minus))
        self.button_multiply = tk.Button(self.button_frame, text="x", font=("Georgia", 26), 
                                         borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                         command=lambda: self.button_functions(self.button_multiply))
        self.button_divide = tk.Button(self.button_frame, text="÷", font=("Georgia", 26), 
                                       borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                       command=lambda: self.button_functions(self.button_divide))
        self.button_equals = tk.Button(self.button_frame, text="=", font=("Georgia", 26), 
                                       borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                       command=lambda: self.button_functions(self.button_equals))
        self.button_backspace = tk.Button(self.button_frame, text="⌫", font=("Georgia", 26), 
                                          borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                          command=lambda: self.button_functions(self.button_backspace))
        self.button_clear = tk.Button(self.button_frame, text="C", font=("Georgia", 26), 
                                      borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                      command=lambda: self.button_functions(self.button_clear))
        self.button_more = tk.Button(self.button_frame, text="More", font=("Georgia", 26), 
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                     command=lambda: self.button_functions(self.button_more))
        self.button_plus_minus = tk.Button(self.button_frame, text="±", font=("Georgia", 26), 
                                           borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                           command=lambda: self.button_functions(self.button_plus_minus))
        self.button_decimal = tk.Button(self.button_frame, text=".", font=("Georgia", 26), 
                                        borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg,
                                        command=lambda: self.button_functions(self.button_decimal))

        #More buttons
        self.button_back = tk.Button(self.more_button_frame, text="Back", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_c_more = tk.Button(self.more_button_frame, text="C", font=("Georgia", 26),
                                              borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_backspace_more = tk.Button(self.more_button_frame, text="⌫", font=("Georgia", 26),
                                              borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_percent = tk.Button(self.more_button_frame, text="%", font=("Georgia", 26),
                                      borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_open_brackert = tk.Button(self.more_button_frame, text="(", font=("Georgia", 26),
                                            borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_close_bracket = tk.Button(self.more_button_frame, text=")", font=("Georgia", 26),
                                            borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_square = tk.Button(self.more_button_frame, text="x²", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_raise_to_n = tk.Button(self.more_button_frame, text="xⁿ", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_factorial = tk.Button(self.more_button_frame, text="x!", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_reciprocal = tk.Button(self.more_button_frame, text="1/x", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_square_root = tk.Button(self.more_button_frame, text="√x", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_nth_root = tk.Button(self.more_button_frame, text="ⁿ√x", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_sin = tk.Button(self.more_button_frame, text="sin", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_cos = tk.Button(self.more_button_frame, text="cos", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_tan = tk.Button(self.more_button_frame, text="tan", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_pi = tk.Button(self.more_button_frame, text="π", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_log = tk.Button(self.more_button_frame, text="log", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_ln = tk.Button(self.more_button_frame, text="ln", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_e = tk.Button(self.more_button_frame, text="e", font=("Georgia", 26),
                                     borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        self.button_equals_more = tk.Button(self.more_button_frame, text="=", font=("Georgia", 26),
                                       borderwidth=0.5, bg=self.frame_bg, activebackground=self.frame_bg)
        
        # Stop the frames from shrinking to the size of children widgets.
        # This fixes issue with label not being packed/anchored properly.
        self.text_frame.grid_propagate(False)
        self.button_frame.grid_propagate(False)
        self.more_button_frame.grid_propagate(False)

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

        self.more_button_frame.grid_rowconfigure(0, minsize=90)
        self.more_button_frame.grid_rowconfigure(1, minsize=90)
        self.more_button_frame.grid_rowconfigure(2, minsize=90)
        self.more_button_frame.grid_rowconfigure(3, minsize=90)
        self.more_button_frame.grid_rowconfigure(4, minsize=90)
        self.more_button_frame.grid_columnconfigure(0, minsize=125)
        self.more_button_frame.grid_columnconfigure(1, minsize=125)
        self.more_button_frame.grid_columnconfigure(2, minsize=125)
        self.more_button_frame.grid_columnconfigure(3, minsize=125)

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

        self.button_back.grid(row=0, column=0, sticky="nsew")
        self.button_c_more.grid(row=0, column=1, sticky="nsew")
        self.button_backspace_more.grid(row=0, column=2, sticky="nsew")
        self.button_percent.grid(row=0, column=3, sticky="nsew")
        self.button_open_brackert.grid(row=1, column=0, sticky="nsew")
        self.button_close_bracket.grid(row=1, column=1, sticky="nsew")
        self.button_square.grid(row=1, column=2, sticky="nsew")
        self.button_raise_to_n.grid(row=1, column=3, sticky="nsew")
        self.button_factorial.grid(row=2, column=0, sticky="nsew")
        self.button_reciprocal.grid(row=2, column=1, sticky="nsew")
        self.button_square_root.grid(row=2, column=2, sticky="nsew")
        self.button_nth_root.grid(row=2, column=3, sticky="nsew")
        self.button_sin.grid(row=3, column=0, sticky="nsew")
        self.button_cos.grid(row=3, column=1, sticky="nsew")
        self.button_tan.grid(row=3, column=2, sticky="nsew")
        self.button_pi.grid(row=3, column=3, sticky="nsew")
        self.button_log.grid(row=4, column=0, sticky="nsew")
        self.button_ln.grid(row=4, column=1, sticky="nsew")
        self.button_e.grid(row=4, column=2, sticky="nsew")
        self.button_equals_more.grid(row=4, column=3, sticky="nsew")

        self.calc_text_label.pack(side="left", anchor="s", padx=10, pady=10)
        self.answer_text_label.pack(side="right", anchor="s", padx=10, pady=10)
        self.previous_text_label.place(relx=0.02, rely=0.75, anchor="sw")
    
    def button_functions(self, button):
        button_text = button.cget("text")
        current_text = self.calc_text_label.cget("text")
        
        if (button_text in self.numbers) or (button_text in self.operators):
                if self.last_pressed_equals:
                    if button_text in self.numbers:
                        self.previous_text_label.config(text=f"({current_text})")
                        self.calc_text_label.config(text=button_text)
                        self.last_pressed_equals = False
                    else:
                        self.previous_text_label.config(text=f"({current_text})")
                        self.calc_text_label.config(text=self.answer_text_label.cget("text") + button_text)
                        self.last_pressed_equals = False
                else:
                    self.calc_text_label.config(text=current_text + button_text)

        elif button_text == "C":
            self.calc_text_label.config(text="")
            self.last_pressed_equals = False
        elif button_text == "⌫":
            self.calc_text_label.config(text=current_text[:-1])
            self.last_pressed_equals = False
        elif button_text == "±":
            self.last_pressed_equals = False
            if current_text.startswith("-"):
                self.calc_text_label.config(text=current_text[1:])
            else:
                self.calc_text_label.config(text="-" + current_text)
        elif button_text == "More":
            self.button_frame.grid_forget()
            self.more_button_frame.grid(row=2, column=0, sticky="nsew")
        elif button_text == "=":
            try:
                duplicates = True
                self.last_pressed_equals = True
                
                while duplicates:
                    if "++" in current_text or "--" in current_text or "xx" in current_text or "÷÷" in current_text:
                        current_text = current_text.replace("++", "+").replace("--", "-").replace("xx", "x").replace("÷÷", "÷")
                    else:
                        duplicates = False

                expression = current_text.replace("x", "*").replace("÷", "/")
                result = eval(expression)

                self.answer_text_label.config(text=str(result))
            except Exception:
                self.last_pressed_equals = True
                self.answer_text_label.config(text="Error")                   
            