import tkinter as tk
from tkinter import ttk

# set up
window = tk.Tk()
window.title('buttons')
window.geometry('600x400')      # widthxheight of window

# button
def button_func():
    print('a basic button bruh')
    print(radio_var.get())

button_string = tk.StringVar(value = 'a button w/ a string var bro')
button = ttk.Button(window, 
                    text = 'a fucking button', 
                    command = button_func, 
                    textvariable = button_string)
button.pack()

# checkbutton
check_var = tk.IntVar(value = 10)
check1 = ttk.Checkbutton(window, 
                        text = 'checkbox1', 
                        command = lambda: print(check_var.get()),
                        variable = check_var,
                        onvalue = 11,
                        offvalue = 00)
check1.pack()

check2 = ttk.Checkbutton(window,
                         text = 'checkbox 2',
                         command = lambda: print('test'))
check2.pack()

# radio buttons
radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(window,
                         text = 'radiobutton1',
                         value = 'radio 1',
                         variable = radio_var,
                         command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window,
                         text = 'radiobutton2',
                         value = 2,
                         variable = radio_var)
radio2.pack()

# exercise 
# create another checkbutton and 2 radiobuttons
# radio button:
    # values for the buttons are A and B
    # ticking either prints the value of the checkbutton
    # ticking the radio button unchecks the checkbutton
# check button:
    # ticking the checkbutton prints the value of the radio button value 
    # use tkinter var for Booleans!
    
# exercie radios

def radio_func():
    print(check_bool.get())
    check_bool.set(False)

# data
radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

# widgets
exercise_radio1 = ttk.Radiobutton(window,
                                  text = 'Radio A',
                                  value = 'A',
                                  command = radio_func, 
                                  variable = radio_string)
exercise_radio2 = ttk.Radiobutton(window,
                                  text = 'Radio B',
                                  value = 'B',
                                  command = radio_func, 
                                  variable = radio_string)

exercise_check = ttk.Checkbutton(window, 
                                 text = 'exercise check', 
                                 variable = check_bool, 
                                 command = lambda: print(radio_string.get()))

# layout
exercise_radio1.pack()
exercise_radio2.pack()
exercise_check.pack()

# run
window.mainloop()