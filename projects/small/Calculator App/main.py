import tkinter as tk
#sympy has to be imported first
from sympy import sympify



class MyCalculator:
    expression = ""

    def __init__(self):
        #create window
        self.window = tk.Tk()

        #set geometry
        self.window.geometry("420x350")

        # prevent size change
        self.window.resizable(height=False, width=False)

        # set background color
        #self.window.configure(background="#000000" )

        # set title
        self.window.title("Calculator")

        # Set font and colors
        self.btn_font = ('Arial', 14)
        self.font = ('Arial', 20)
        self.bg_color = '#282c34'
        self.fg_color = '#ffffff'
        self.button_color = '#61afef'
        self.button_fg_color = '#ffffff'
        self.bg_entry_color = '#1e2127'
        self.bg_answer_color = '#000000'


        # set variables to hold results
        self.equation = tk.StringVar()
        self.answer = tk.StringVar()

        #set the entry field for the calculation
        self.entrybox = tk.Entry(self.window, textvariable=self.equation, font=self.font, bg = self.bg_entry_color, fg=self.fg_color, relief="raised")
        self.entrybox.pack(padx=10,fill="both")

        self.answerbox = tk.Entry(self.window, textvariable=self.answer, font=self.font, bg = self.bg_answer_color, fg=self.bg_entry_color, relief="sunken", state="readonly")
        self.answerbox.pack(padx=10,fill="both")



        # let's begin by creating a frame
        self.buttonframe = tk.Button(self.window, bg=self.bg_color)
        
        # Configure the grid layout of the frame

        # configure the number of columns
        for i in range(4):
            self.buttonframe.columnconfigure(i, weight=1)
        # configure the number of row
        for i in range(5):
            self.buttonframe.rowconfigure(i, weight=1)

        # create a function that will add the buttons
        self.create_buttons()

        self.buttonframe.pack(fill="both", padx=10, pady=10)

        # Start the main loop
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
            self.result = "Error"
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
                btn = tk.Button(self.buttonframe, text=text,command = self.clear, font=self.btn_font, bg=self.button_color, fg=self.button_fg_color, relief='raised')
            elif text == "<<":
                btn = tk.Button(self.buttonframe, text=text,command = self.backspace, font=self.btn_font, bg=self.button_color, fg=self.button_fg_color, relief='raised')
            elif text ==  "=":
                btn = tk.Button(self.buttonframe, text=text,command = self.calculate, font=self.btn_font, bg=self.button_color, fg=self.button_fg_color, relief='raised')
                
            else:
                btn = tk.Button(self.buttonframe, text=text,command = lambda t=text: self.press(t), font=self.btn_font, bg=self.button_color, fg=self.button_fg_color, relief='raised')
            btn.grid(column=col, row=row, sticky=tk.W + tk.E +tk.N +tk.S, padx=5, pady=5)





MyCalculator()
