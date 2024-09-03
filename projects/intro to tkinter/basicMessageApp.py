import tkinter as tk
from tkinter import messagebox

## we will need a class for the GUI

class MyGUI:
    def __init__(self):
        self.window01 = tk.Tk()

        #set geometry
        self.window01.geometry("800x500")

        #set title
        self.window01.title("Text Box")

        # set a menu
        self.menubar = tk.Menu(self.window01)
        
        # lets create a menu inside the  first menu
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
         # let's add commands into the file menu
        self.filemenu.add_command(label="Close", command=self.on_closing)

        # in order to add this emnu, we need to 
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # we configure the window01 to add this to our GUI window01
        self.window01.config(menu=self.menubar)

        # set first label
        self.label01 = tk.Label(self.window01, text="Enter any text",font=("Arial", 16))
        self.label01.pack(padx =15, pady=15)
        # insert text box
        self.textbox01 = tk.Text(self.window01, height=3,font=("Arial", 12))
        #this bind will support our shortcut funnction later on
        #bind helps show the working state of whatever is passed into it
        # in this case we want to know the KeyPress state
        self.textbox01.bind("<KeyPress>", self.shortcut)
        self.textbox01.pack(padx =15)



        # check button
        # to use the check button, we need to add a variable to the check button
        # we ususally use the tk.IntVar
        self.checkbox_state = tk.IntVar()
        # now let's add the actual check button
        self.checkbox01 = tk.Checkbutton(self.window01, text="Display Text", font=("Arial", 12), variable=self.checkbox_state)
        self.checkbox01.pack()

        # insert button
        self.button01 = tk.Button(self.window01,text="Display message",font=("Arial", 16), command = self.displaytext)
        self.button01.pack()

        #clear button
        self.clearbtn = tk.Button(self.window01,text="Clear",font=("Arial", 12), command = self.cleartext)
        self.clearbtn.pack(padx=10,pady=10)


        ######################################################
        # for the closing message function that will created later on
        self.window01.protocol("WM_DELETE_WINDOW", self.on_closing)

        ########################################################
        self.window01.mainloop()



    ##################################
    # let's create a new function that will show the display the text
    def displaytext(self): 
        #this function is supposed to work after we click button01
        # as such we will add command = self.displaytext to the button function
        self.checkbox_state.get()
        # check box is 0 when not checked
        if self.checkbox_state.get() == 0:
            # to get value from the very first text, we use "1.0"
            # and to end at the last text we use tk.END
            print(self.textbox01.get("1.0", tk.END))
        else:
            # if it has been checked, we will se a message box
            messagebox.showinfo(title="Your Message", message=self.textbox01.get("1.0", tk.END))



    #############################################
    # let's say you want to have a shortcut
    # a shortcut that allows you to display text
    # example when i click CTRL + ENTER

    #in such a case, we will have to create a new function and add an event
    # the even will occur while you type and as such will be bound to the textbox

    def shortcut(self, event):
        # event.keysym and event.state are the two func we will use to determine 
        #if both CTRL nd ENTER have been pressed
        if event.state== 12 and event.keysym== "Return":
            self.displaytext()

    
    #################################################
    # to create a pop up menu when ever you decide to close the page, 
    # we will have to create a new function
    # this function will be linked

    def on_closing(self):
        # first we should give the user the option or choosing whether they really want to quit
        if messagebox.askyesno(title="Quit??", message="Do you want to quit?"):
            # we can destroy or close window now
            self.window01.destroy()



    ##########################################################
    # this function will work with the clear button to clear all data in the text box

    def cleartext(self):
        self.textbox01.delete("1.0",tk.END)


############################################################################
    if __name__ == __init__:
        __init__()


MyGUI()
