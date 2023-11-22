#coding:utf-8
import zipfile
a=0
total=0
with zipfile.ZipFile('sample.zip',"r") as zf:
    name = zf.namelist()
    for i in name:
        if i.endswith("_kgu.txt"):
            with zf.open(i,"r") as f:
                number = f.read()
                
                if a%2 == 1:
                    total += int(number)
                a +=1
print(total)
    
