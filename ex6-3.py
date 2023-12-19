#coding:utf-8
import zipfile
import json
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=2000,height=1000,bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)


def load_data(number):
    file_name = f'kabeposter/kabeposter_{number:012d}_keypoints.json'
    with zipfile.ZipFile('kabeposter.zip', 'r') as zf:
        with zf.open(file_name, 'r') as f:
            frame_data = json.load(f)
    
    return frame_data
    

data = [[[[0 for _ in range(3)] for _ in range(25)] for _ in range(2)] for _ in range(100)]
for h in range(100):
    file_data=load_data(h)
    for i in range(2):
        keypoints = file_data['people'][i]['pose_keypoints_2d']
        for j in range(25):
            data[h][i][j][0] = keypoints[j * 3]
            data[h][i][j][1] = keypoints[j * 3 + 1]
            data[h][i][j][2] = keypoints[j * 3 + 2]

def create_line(h,i):
    if data[h][i][0][2] and data[h][i][1][2] > 0:
        canvas.create_line(data[h][i][0][0],data[h][i][0][1],data[h][i][1][0],data[h][i][1][1],width=2)
    if data[h][i][1][2] and data[h][i][2][2]> 0:
        canvas.create_line(data[h][i][1][0],data[h][i][1][1],data[h][i][2][0],data[h][i][2][1],width=2)
    if data[h][i][5][2] and data[h][i][1][2]> 0:
        canvas.create_line(data[h][i][1][0],data[h][i][1][1],data[h][i][5][0],data[h][i][5][1],width=2)
    if data[h][i][1][2] and data[h][i][3][2]> 0:
        canvas.create_line(data[h][i][2][0],data[h][i][2][1],data[h][i][3][0],data[h][i][3][1],width=2)
    if data[h][i][3][2] and data[h][i][4][2]> 0:
        canvas.create_line(data[h][i][3][0],data[h][i][3][1],data[h][i][4][0],data[h][i][4][1],width=2)
    if data[h][i][5][2] and data[h][i][6][2]> 0:
        canvas.create_line(data[h][i][5][0],data[h][i][5][1],data[h][i][6][0],data[h][i][6][1],width=2)
    if data[h][i][6][2] and data[h][i][7][2]> 0:
        canvas.create_line(data[h][i][6][0],data[h][i][6][1],data[h][i][7][0],data[h][i][7][1],width=2)
    if data[h][i][1][2] and data[h][i][8][2]> 0:
        canvas.create_line(data[h][i][1][0],data[h][i][1][1],data[h][i][8][0],data[h][i][8][1],width=2)
    if data[h][i][8][2] and data[h][i][9][2]> 0:
        canvas.create_line(data[h][i][8][0],data[h][i][8][1],data[h][i][9][0],data[h][i][9][1],width=2)
    if data[h][i][8][2] and data[h][i][12][2]> 0:
        canvas.create_line(data[h][i][8][0],data[h][i][8][1],data[h][i][12][0],data[h][i][12][1],width=2)
    if data[h][i][9][2] and data[h][i][10][2]> 0:
        canvas.create_line(data[h][i][9][0],data[h][i][9][1],data[h][i][10][0],data[h][i][10][1],width=2)
    if data[h][i][10][2] and data[h][i][11][2]> 0:
        canvas.create_line(data[h][i][10][0],data[h][i][10][1],data[h][i][11][0],data[h][i][11][1],width=2)
    if data[h][i][11][2] and data[h][i][24][2]> 0:
        canvas.create_line(data[h][i][11][0],data[h][i][11][1],data[h][i][24][0],data[h][i][24][1],width=2)
    if data[h][i][11][2] and data[h][i][22][2]> 0:
        canvas.create_line(data[h][i][11][0],data[h][i][11][1],data[h][i][22][0],data[h][i][22][1],width=2)
    if data[h][i][22][2] and data[h][i][23][2]> 0:
        canvas.create_line(data[h][i][22][0],data[h][i][22][1],data[h][i][23][0],data[h][i][23][1],width=2)
    if data[h][i][12][2] and data[h][i][13][2]> 0:
        canvas.create_line(data[h][i][12][0],data[h][i][12][1],data[h][i][13][0],data[h][i][13][1],width=2)
    if data[h][i][13][2] and data[h][i][14][2]> 0:
        canvas.create_line(data[h][i][13][0],data[h][i][13][1],data[h][i][14][0],data[h][i][14][1],width=2)
    if data[h][i][14][2] and data[h][i][21][2]> 0:
        canvas.create_line(data[h][i][14][0],data[h][i][14][1],data[h][i][21][0],data[h][i][21][1],width=2)
    if data[h][i][14][2] and data[h][i][19][2]> 0:
        canvas.create_line(data[h][i][14][0],data[h][i][14][1],data[h][i][19][0],data[h][i][19][1],width=2)
    if data[h][i][5][2] and data[h][i][1][2]> 0:
        canvas.create_line(data[h][i][19][0],data[h][i][19][1],data[h][i][20][0],data[h][i][20][1],width=2)
    if data[h][i][0][2] and data[h][i][15][2]> 0:
        canvas.create_line(data[h][i][0][0],data[h][i][0][1],data[h][i][15][0],data[h][i][15][1],width=2)
    if data[h][i][0][2] and data[h][i][16][2]> 0:
        canvas.create_line(data[h][i][0][0],data[h][i][0][1],data[h][i][16][0],data[h][i][16][1],width=2)
    if data[h][i][15][2] and data[h][i][17][2]> 0:
        canvas.create_line(data[h][i][15][0],data[h][i][15][1],data[h][i][17][0],data[h][i][17][1],width=2)
    if data[h][i][16][2] and data[h][i][18][2]> 0:
        canvas.create_line(data[h][i][16][0],data[h][i][16][1],data[h][i][18][0],data[h][i][18][1],width=2)

def animate(frame_number=0):
    canvas.delete("all")  # アニメーションのたびにキャンバスをクリア

    for i in range(2):
        create_line(frame_number, i)

    frame_number += 1
    if frame_number < 100:
        root.after(50, animate, frame_number)  # アニメーション速度を調整

animate()  # アニメーションを開始
root.mainloop()