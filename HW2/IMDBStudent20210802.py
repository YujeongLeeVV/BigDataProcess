#!/usr/bin/python3
import sys

movieInput=sys.argv[1]
movieOutput=sys.argv[2]


list1=[]
dic={}


with open(movieInput, "rt") as fd:
    data=fd.read()
    lines=data.splitlines()
    for line in lines:
        movieInfo=line.split("::")
        genre=movieInfo[2]
        if genre in dic.keys():
            dic[genre]+=1
        else:
            dic[genre]=1
        
        
with open(movieOutput, "wt") as f:
    for key, value in dic.items():
        f.write(f"{key} {value}\n")
