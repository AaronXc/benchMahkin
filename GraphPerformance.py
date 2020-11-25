#to run on my machine and generate plots of the sppeeeedddd
#C:/Users/Aaron Wilcox/script_dvelopment/benchmarking/ the path to the BenchMKresults file

import subprocess
import re
import os
import sys
import matplotlib.pyplot as plt
import  numpy as np
import time

f=open("BenchMKresults", "r")
y_axis = []
x_axis = []
data = []
i=0
filename=f.readline().strip()
path = filename.replace(" ", "")
descName=input("please enter a descriptive name for the test. This will be the name of the directory containing the results of the test ")
path=descName
while os.path.exists("./AutoSavedResults/"+path) != False:
    warning="A directory named "+path+" already exists. Please enter a different name"
    path = input(warning)
results = f.readlines()
f.close()
if os.path.exists("./AutoSavedResults") == False:
    os.mkdir("./AutoSavedResults")
os.mkdir("./AutoSavedResults/"+path)
data=open("./AutoSavedResults/"+path+"/"+filename, "w+")
for line in results:
    data.write(line)
data.close()
ALLtheData=[]
x_axis=[]
IOPS_y_axis=[] 
BW_y_axis=[]   
for line in results:
    throughput = re.search("(\d+),(\d+\.*\d+),(\d+\.*\d+)", line)
    if throughput != None:
        if throughput.group(1) not in x_axis:
            x_axis.append(throughput.group(1))
        ALLtheData.append((throughput.group(1), throughput.group(2), throughput.group(3)))   
print("all the data: ", ALLtheData)  
for dataPoint in ALLtheData:
    if dataPoint != "used":
        IOPSdata = float(dataPoint[1])
        BWdata = float(dataPoint[2])
        temp = ["blank"]
        for j in range(ALLtheData.index(dataPoint)+1, len(ALLtheData)):
            if ALLtheData[j] != None and ALLtheData[j][0] == dataPoint[0]:
                temp.append("blank")
                IOPSdata+=float(ALLtheData[j][1])
                BWdata+=float(ALLtheData[j][2])
                ALLtheData[j]="used"
        BWdata=BWdata/len(temp)
        IOPSdata=IOPSdata/len(temp)
        print("IOPS: ", IOPSdata)
        print("BW: ", BWdata)        
        index=ALLtheData.index(dataPoint)
        print("index: ", index)
        x_val = dataPoint[0]
        ALLtheData.remove(dataPoint) 
        ALLtheData.insert(index, (x_val, IOPSdata, BWdata))

print(ALLtheData)
print(x_axis)
averages = open("./AutoSavedResults/"+path+"/"+"average values.txt", "a+")
for x_val in x_axis:
    for dataPoint in ALLtheData:
        if dataPoint[0] == x_val:
            IOPS_y_axis.append(dataPoint[1])
            BW_y_axis.append(dataPoint[2])
            BW=str(dataPoint[2])
            IOPS=str(dataPoint[1])
            averages.write(dataPoint[0]+","+IOPS+","+BW+"\n")
averages.close()
"""
if options.iops == True and options.bw == False:
    y_axis.append(throughput.group(3))
elif options.iops == False and options.bw == True:
    y_axis.append(throughput.group(3))
elif options.iops == True and options.bw == True:
    #plot two lines on the same graph
"""            

skip=2
locations=(np.arange(1,len(x_axis), skip))
labels=[]
for loc in locations:
    labels.append(str(loc))   
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle("Stornado Performance")
ax1.plot(x_axis, IOPS_y_axis, "tab:red")
ax2.plot(x_axis, BW_y_axis)
plt.xlabel("number of drives used in I/O operations")
ax1.set(ylabel="IOPS (operations/s)")
ax2.set(ylabel="throughput (MiB/s)")
ax1.set_xticks(ticks=locations)
ax2.set_xticks(ticks=locations)
ax1.grid(True)
ax2.grid(True)
#plt.show()
plt.savefig("./AutoSavedResults/"+path+"/"+path+"graphs.png")
f=open("./benchMKresults", "r+")
lines = f.readlines()
f.close()
f=open("./AutoSavedResults/"+path+"/allResults", "w+")
for line in lines:
    f.write(line+"\n")
f.close()









