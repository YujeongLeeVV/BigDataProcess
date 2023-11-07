#!/usr/bin/python3
import datetime
taxi=[]
dic={}

uberInput=input()
uberOutput=input()

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
                
            f.write(f"{uberInfo[0]},{day} {uberInfo[2]},{uberInfo[3]}\n")
        

