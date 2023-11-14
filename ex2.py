#coding:utf-8
import json


with open("catalog.json", "r") as file:
    data = json.load(file)
    
price = [item["price"] for item in data if item["name"] == "jacket"]

count = len(price)

max=max(price)
min=min(price)

print(f'個数: {count}')
print(f'最高価格: {max}')
print(f'最低価格: {min}')