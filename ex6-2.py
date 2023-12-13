#coding:utf-8
import zipfile
import json
import tkinter as tk


with zipfile.ZipFile('kabeposter.zip',"r") as zf:
    name = zf.namelist()
    for i in name:
        if i.endswith("00_keypoints.json"):
            with zf.open(i,"r") as f:
                 data = json.load(f)

people_data = data["people"]

shoulder1 = [
    int(people_data[0]["pose_keypoints_2d"][6]), int(people_data[0]["pose_keypoints_2d"][7]),
    int(people_data[0]["pose_keypoints_2d"][3]), int(people_data[0]["pose_keypoints_2d"][4])]

shoulder2 = [
    int(people_data[0]["pose_keypoints_2d"][3]), int(people_data[0]["pose_keypoints_2d"][4]),
    int(people_data[0]["pose_keypoints_2d"][15]), int(people_data[0]["pose_keypoints_2d"][16])]

shoulder3 = [
    int(people_data[1]["pose_keypoints_2d"][6]), int(people_data[1]["pose_keypoints_2d"][7]),
    int(people_data[1]["pose_keypoints_2d"][3]), int(people_data[1]["pose_keypoints_2d"][4])]

shoulder4 = [
    int(people_data[1]["pose_keypoints_2d"][3]), int(people_data[1]["pose_keypoints_2d"][4]),
    int(people_data[1]["pose_keypoints_2d"][15]), int(people_data[1]["pose_keypoints_2d"][16])]

root = tk.Tk()

canvas = tk.Canvas(root, width=2000,height=1000,bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

def draw_shoulder_line(canvas, shoulder):
    canvas.create_line(shoulder[0], shoulder[1], shoulder[2], shoulder[3], fill="red", width=2)
    
def draw_shoulder_line2(canvas, shoulder):
    canvas.create_line(shoulder[0], shoulder[1], shoulder[2], shoulder[3], fill="green", width=2)    
    
draw_shoulder_line(canvas, shoulder1)
draw_shoulder_line2(canvas, shoulder2)
draw_shoulder_line(canvas, shoulder3)
draw_shoulder_line2(canvas, shoulder4)

# イベントループの開始
root.mainloop()