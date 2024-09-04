import tkinter as tk
from tkinter import messagebox
#sympy has to be imported first
from sympy import sympify



class MyCalculator:
    expression = ""

    def __init__(self):
        #create window
        self.window = tk.Tk()

        #set geometry
        self.window.geometry("300x180")

        # set title
        self.window.title("Calculator")

        #
        self.equation = tk.StringVar()

        #
        self.answer = tk.StringVar()

        #set the entry field for the calculation
        self.entrybox = tk.Entry(self.window, textvariable=self.equation)
        self.entrybox.pack(padx=10, fill="x")
        self.answerbox = tk.Entry(self.window, textvariable=self.answer, state="readonly")
        self.answerbox.pack(padx=10, fill="x")



        # let's begin by creating a frame
        self.buttonframe = tk.Button(self.window)
        # configure the number of columns
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        # create a function that will add the buttons
        self.create_buttons()

        self.buttonframe.pack(fill="both")

        self.window.mainloop()

    def press(self, num):
        global expression
        
        self.expression += str(num)

        self.equation.set(self.expression)

    
    def calculate(self):
        # since some of our users might not have installed sympify yet, we can try using eval first and use sympify if an error pops up
        try:
            self.expression.lstrip("0")
            self.result = sympify(self.expression).evalf()
            
            self.result = f"{float(self.result):.2f}"
        except Exception as e:
            self.result = f"Error: {e}"
        self.answer.set(self.result)
        
    def backspace(self):
        # we delete that last input
        # we can then reassign expression as everything in self.expression except the last input
        self.expression = self.expression[:-1]
        # self.equation.set("")
        self.equation.set(self.expression)
    
    def clear(self):
        # we delete that last input
        # we can then reassign expression as everything in self.expression except the last input
        self.expression = ""
        self.equation.set(self.expression)
        self.answer.set(0)


    def create_buttons(self):
        buttons = [
            ('(', 0, 0), (')', 1, 0), ('<<', 2, 0), ('C', 3, 0),
            ('1', 0, 1), ('2', 1, 1), ('3', 2, 1), ('+', 3, 1),
            ('4', 0, 2), ('5', 1, 2), ('6', 2, 2), ('-', 3, 2),
            ('7', 0, 3), ('8', 1, 3), ('9', 2, 3), ('*', 3, 3),
            ('/', 0, 4), ('0', 1, 4), ('.', 2, 4), ('=', 3, 4)
        ]

        for (text, col, row) in buttons:
            if text == "C":
                btn = tk.Button(self.buttonframe, text=text,command = self.clear)
            elif text == "<<":
                btn = tk.Button(self.buttonframe, text=text,command = self.backspace)
            elif text ==  "=":
                btn = tk.Button(self.buttonframe, text=text,command = self.calculate)
                
            else:
                btn = tk.Button(self.buttonframe, text=text,command = lambda t=text: self.press(t))
            btn.grid(column=col, row=row, sticky=tk.W + tk.E)





MyCalculator()
