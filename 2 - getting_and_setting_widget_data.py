import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    entry_text = entry.get()
    
    # update the label
    #label.configure(text = 'other text')
    label ['text'] = entry_text
    entry ['state'] = 'disabled'
    #print(label.configure())

# window
window = tk.Tk()
window.title('getting and setting widgets')

# widgets 
label = ttk.Label(master = window, text = 'text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'set', command = button_func)
button.pack()

def reset_func():
    label['text'] = 'some text'
    entry['state'] = 'enabled'

button2 = ttk.Button(master = window, text = 'reset', command = reset_func)
button2.pack()

# run
window.mainloop()