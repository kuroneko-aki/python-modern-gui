import tkinter as tk
from tkinter import ttk

def button_func1():
    print('you pressed a button')
def button_func2():
    print('hello')

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label (a sub-module of tkinter)
label1 = ttk.Label(master = window, text = 'This is a test')
label1.pack()

# tk.text
text = tk.Text(master = window)
text.pack()

# ttk entry 
entry = ttk.Entry(master = window)
entry.pack()

label2 = ttk.Label(master = window, text = 'my label')
label2.pack()

# ttk button
button1 = ttk.Button(master = window, text = 'button', command = button_func1)
button1.pack()
button2 = ttk.Button(master = window, text = 'another button', command = button_func2)
button2.pack()

# run
window.mainloop()