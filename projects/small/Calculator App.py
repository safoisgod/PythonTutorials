import tkinter as tk
from tkinter import messagebox

class MyCalculator:
    expression = ""
    def press(num):
        expression += str(num)



    def __init__(self):
        #create window
        self.window = tk.Tk()

        #set geometry
        self.window.geometry("300x180")

        # set title
        self.window.title("Calculator")

        #set the entry field for the calculation
        entrybox = tk.Entry(self.window, textvariable="Enter Equation")
        entrybox.pack(padx=10, fill="x")
        answerbox = tk.Entry(self.window)
        answerbox.pack(padx=10, fill="x")


        # let's begin by creating a frame
        self.buttonframe = tk.Button(self.window)
        # configure the number of columns
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        # create buttons for numbers and arithmetic functions
        # ROW 1
        button1 = tk.Button(self.buttonframe, text="1")
        button1.grid(column=0, row=0, sticky=tk.W + tk.E)
        button2 = tk.Button(self.buttonframe, text="2")
        button2.grid(column=1, row=0, sticky=tk.W + tk.E)
        button3 = tk.Button(self.buttonframe, text="3")
        button3.grid(column=2, row=0, sticky=tk.W + tk.E)
        addbtn = tk.Button(self.buttonframe, text="+")
        addbtn.grid(column=3, row=0, sticky=tk.W + tk.E)

        # ROW 2
        button4 = tk.Button(self.buttonframe, text="4")
        button4.grid(column=0, row=1, sticky=tk.W + tk.E)
        button5 = tk.Button(self.buttonframe, text="5")
        button5.grid(column=1, row=1, sticky=tk.W + tk.E)
        button6 = tk.Button(self.buttonframe, text="6")
        button6.grid(column=2, row=1, sticky=tk.W + tk.E)
        subbtn = tk.Button(self.buttonframe, text="-")
        subbtn.grid(column=3, row=1, sticky=tk.W + tk.E)

        # ROW 3
        button7 = tk.Button(self.buttonframe, text="7")
        button7.grid(column=0, row=2, sticky=tk.W + tk.E)
        button8 = tk.Button(self.buttonframe, text="8")
        button8.grid(column=1, row=2, sticky=tk.W + tk.E)
        button9 = tk.Button(self.buttonframe, text="9")
        button9.grid(column=2, row=2, sticky=tk.W + tk.E)
        multbtn = tk.Button(self.buttonframe, text="x")
        multbtn.grid(column=3, row=2, sticky=tk.W + tk.E)

        # ROW 4
        divbtn = tk.Button(self.buttonframe, text="/")
        divbtn.grid(column=0, row=3, sticky=tk.W + tk.E)
        button0 = tk.Button(self.buttonframe, text="0")
        button0.grid(column=1, row=3, sticky=tk.W + tk.E)
        decbtn = tk.Button(self.buttonframe, text=".")
        decbtn.grid(column=2, row=3, sticky=tk.W + tk.E)
        ansbtn = tk.Button(self.buttonframe, text="=")
        ansbtn.grid(column=3, row=3, sticky=tk.W + tk.E)

        # ROW 5
        sqrbtn = tk.Button(self.buttonframe, text="x\N{SUPERSCRIPT TWO}'")
        sqrbtn.grid(column=0, row=4, sticky=tk.W + tk.E)
        percbtn = tk.Button(self.buttonframe, text="%")
        percbtn.grid(column=1, row=4, sticky=tk.W + tk.E)
        backspacebtn = tk.Button(self.buttonframe, text="<<")
        backspacebtn.grid(column=2, row=4, sticky=tk.W + tk.E)
        clrbtn = tk.Button(self.buttonframe, text="C")
        clrbtn.grid(column=3, row=4, sticky=tk.W + tk.E)



        self.buttonframe.pack(fill="x")



        self.window.mainloop()

        

    if __name__ == __init__:
        __init__()
    


MyCalculator()
