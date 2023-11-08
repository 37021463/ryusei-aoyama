#coding:utf-8

# ファイルを開く
with open("data.txt", "r") as file:
    total = 0  

    
    for line in file:
        try:
            total += int(line.strip())
        except ValueError:
            pass

print("整数の合計:", total)
