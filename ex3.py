#coding:utf-8
import json

with open("catalog.json") as f:
    j = json.load(f)

x = next((item["price"] for x in j if x["name"] == "jacket"),None)

coumt = len(x)
max = 