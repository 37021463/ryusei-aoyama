import tkinter as tk
import time

root = tk.Tk()

canvas = tk.Canvas(root, width=300,height=400,bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

head=canvas.create_oval(140, 50, 160, 70, fill="white")
body=canvas.create_line(150, 70, 150, 150, fill="black")
leftleg=canvas.create_line(150, 150, 130, 200, fill="black")
rightleg=canvas.create_line(150, 150, 170, 200, fill="black")
leftarm=canvas.create_line(150, 100, 120, 60, fill="black")
rightarm=canvas.create_line(150, 100, 180, 60, fill="black")

dx = 5
dy = 0

def move():
    canvas.move(head,dx,dy)
    canvas.move(body,dx,dy)
    canvas.move(leftleg,dx,dy)
    canvas.move(rightleg,dx,dy)
    canvas.move(leftarm,dx,dy)
    canvas.move(rightarm,dx,dy)
    canvas.after(100, move)
    
move()
root.mainloop()