import tkinter as tk
from tkinter import ttk

# window 
window = tk.Tk()
window.geometry('600x400')
window.title('Treeview')

# data 
first_names = ['Eren', 'Mikasa', 'Armin', 'Levi', 'Hange', 'Ymir', 'Crista']
last_names = ['Jeager', 'Ackerman', 'Arlert', 'Ackerman', 'Zoe', 'Fritz', 'Reiss']

# treeview
table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show='headings')
table.heading('first', text='First Name')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack()

# run
window.mainloop()