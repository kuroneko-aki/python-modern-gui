# A canvas is a widget that allows you to 'draw' shapes
# Like drawing squares, circles, lines, etc.

import tkinter as tk 

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')

#canvas
canvas = tk.Canvas(window, bg = 'red')
canvas.pack()

canvas.create_rectangle((50, 20, 100, 200), fill = 'blue', width = 5, outline = 'green') #left, top, right, bottom
canvas.create_oval((200, 0, 300, 100), fill = 'pink')    # left, top, right, bottom
canvas.create_line((0, 0, 100, 150), fill = 'yellow')      # start_x, start_y, end_x, end_y
canvas.create_polygon((0,0, 100,200, 300,50))   # x1,y1, x2,y2, x3,y3
# run
window.mainloop()