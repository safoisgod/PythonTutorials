import tkinter as tk

#create a window uning tk.Tk()
window01 = tk.Tk()

# we set a geometry
window01.geometry("500x500")

#set a title
window01.title("My first GUI")

# to set up a layout we can use PACK or GRID

##########################################################
# to create a widget that contains text or to add text to your window, use tk.Label
label01 = tk.Label(window01, text="Welcome",font=("Arial",16))

# to apply this label in the GUI, we can use the PACK
#we add the padding around it using PADX and PADY
label01.pack(padx=15, pady=15)

###########################################################
# next, let's add a text box
# this box will take in an input 
#  this is useful for a multiline inputs
textbox01 = tk.Text(window01, height= 10, font=("Arial",12))
textbox01.pack(padx=15)

############################################################
# for single line and smaller "textboxs" we can use ENTRY
entry01 = tk.Entry(window01) 
entry01.pack(pady=15)


###########################################################
# to add a button we use the .BUTTON
button01 = tk.Button(window01, text="Enter",font=("Arial", 12))
button01.pack()

############################################################
# in the instance of building a calculator programme, we will more than 1 button in a single frame
# in such a case, we can have something like a grid
# to have such instance, we have to create and define a frame, be fore creating our buttons

buttonframe01 = tk.Frame(window01)
# to configure the various columns in the frame, we use .COLUMNCONFIGURE
# we set the weight to 1
# a non zero weight means the column expands to fill in any space that reamins
# if it is set to 0 is will have a fixed width

# we need three columns so we will have to configure the frame three times
buttonframe01.columnconfigure(0, weight=1)
buttonframe01.columnconfigure(1, weight=1)
buttonframe01.columnconfigure(2, weight=1)


# next let's insert the buttons into the button frames
# we pass the buttonframe as tha master instead of the window01
btn01 = tk.Button(buttonframe01, text="1", font=("Arial", 10))
# since we will be representing each button in a grid kind frame we use the .GRID
# secondly to get a stretchy button we can use STICKY
btn01.grid(row=0,column=0, sticky=tk.W+tk.E)

btn02 = tk.Button(buttonframe01, text="2", font=("Arial", 10))
btn02.grid(row=0,column=1, sticky=tk.W+tk.E)
btn03 = tk.Button(buttonframe01, text="3", font=("Arial", 10))
btn03.grid(row=0,column=2, sticky=tk.W+tk.E)
btn04 = tk.Button(buttonframe01, text="4", font=("Arial", 10))
btn04.grid(row=1,column=0, sticky=tk.W+tk.E)
btn05 = tk.Button(buttonframe01, text="5", font=("Arial", 10))
btn05.grid(row=1,column=1, sticky=tk.W+tk.E)
btn06 = tk.Button(buttonframe01, text="6", font=("Arial", 10))
btn06.grid(row=1,column=2, sticky=tk.W+tk.E)


# to apply the spread over the x axis, use the fill="x"
buttonframe01.pack(fill="x")


# as seen, GRID and PACK have a structure they follow
# in order to place your button or textbox exactly where you want it to be, you can use .PLACE
button02 = tk.Button(window01, text="hahaha", font=("Arial", 12))
button02.place(x=200, y=200, height= 50, width=50)

# mainloop() is used when the application has been completed and is ready to run
window01.mainloop()
