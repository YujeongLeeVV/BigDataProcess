#!/usr/bin/python3
import datetime
import sys
taxi=[]
dic={}

uberInput=sys.argv[1]
uberOutput=sys.argv[2]

with open(uberInput, "rt") as fd:
    with open(uberOutput, "wt") as f:
        data=fd.read()
        lines=data.splitlines()
        for line in lines:
            uberInfo=line.split(",")
            date=uberInfo[1]
            dateLines=date.split("/")

            day=datetime.date(int(dateLines[2]), int(dateLines[0]), int(dateLines[1])).weekday()
            if day==0:
                day="MON"
            elif day==1:
                day="TUE"
            elif day==2:
                day="WED"
            elif day==3:
                day="THU"
            elif day==4:
                day="FRI"
            elif day==5:
                day="SAT"
            else:
                day="SUN"
                
            region=uberInfo[0]
            
            if region in dic:
                dic[region]+=f"{region},{day} {uberInfo[2]},{uberInfo[3]}\n"
            else:
                dic[region]=f"{region},{day} {uberInfo[2]},{uberInfo[3]}\n"
            
        for value in dic.values():
            f.write(f"{value}")
        

