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
            vehicle=uberInfo[2]
            trip=uberInfo[3]
            
            if (region, day, 1) in dic:
                dic[region, day, 0]+=int(vehicle)
                dic[region, day, 1]+=int(trip)
                
            else:
                dic[region, day, 0]=int(vehicle)
                dic[region, day, 1]=int(trip)
        
        i=0            
        
        for key in dic.keys():
            #f.write(f"{key}, {value}\n")
            if i%2==0:
                f.write(f"{key[0]},{key[1]} {dic[key[0],key[1],0]},{dic[key[0],key[1],1]}\n")
            i+=1
