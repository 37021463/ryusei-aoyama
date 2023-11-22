import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=300,height=400,bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_oval(140, 50, 160, 70, fill="white")
canvas.create_line(150, 70, 150, 150, fill="black")
canvas.create_line(150, 150, 130, 200, fill="black")
canvas.create_line(150, 150, 170, 200, fill="black")
canvas.create_line(150, 100, 120, 60, fill="black")
canvas.create_line(150, 100, 180, 60, fill="black")

root.mainloop()