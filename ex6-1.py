#coding:utf-8
import zipfile
import json

with zipfile.ZipFile('kabeposter.zip',"r") as zf:
    name = zf.namelist()
    for i in name:
        if i.endswith("00_keypoints.json"):
            with zf.open(i,"r") as f:
                 data = json.load(f)
  
    keypoints = data["people"][0]["pose_keypoints_2d"]
    nose = keypoints[0*3:(0+1)*3]
    neck = keypoints[1*3:(1+1)*3]
    
    print(f"鼻{nose}")
    print(f"首{neck}")
    
    keypoints = data["people"][1]["pose_keypoints_2d"]
    nose = keypoints[0*3:(0+1)*3]
    neck = keypoints[1*3:(1+1)*3]
    
    print(f"鼻{nose}")
    print(f"首{neck}")