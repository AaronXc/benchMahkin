#to run on my machine and generate plots of the sppeeeedddd
#C:/Users/Aaron Wilcox/script_dvelopment/benchmarking/ the path to the BenchMKresults file

import subprocess
import re
import os
import matplotlib.pyplot as plt
import  numpy as np
import shutil
from benchMKscriptVars import noAlternating, alternatingPorts, alternatingPortsAndCards, alternatingCards, directoryNames, globalSection, globalSection2, globalSection3, globalSections, driveOrders


ioType = ["/reads", "/writes"]

hardware=open("./BenchMKresults/hardware", "r+")
path=hardware.readline()  
path=path.strip()                                          # path is where the results for the test will be saved
hardware.close()

if os.path.exists("./AutoSavedResults") == False:
    os.mkdir("./AutoSavedResults")
if os.path.exists("./AutoSavedResults/"+path) == False:
    os.mkdir("./AutoSavedResults/"+path)

json=open("./BenchMKresults/allResults.json", "r+")
jsonData=json.readlines()
json.close()

json=open("./AutoSavedResults/"+path+"/allResults.json", "w+")
for line in jsonData:
    json.write(line)
json.close()

for section in globalSections:
    for driveOrder in driveOrders:
        directoryNameIndex = driveOrders.index(driveOrder)+len(driveOrders)*globalSections.index(section)
        
        testName="BenchMKresults_"+directoryNames[directoryNameIndex]
        os.mkdir("./AutoSavedResults/"+path+"/"+testName)
        
        for io in ioType:
            if os.path.exists("BenchMKresults/"+testName+io):
                graph_Coordinates_to_be=open("BenchMKresults/"+testName+io, "r") 
                results = graph_Coordinates_to_be.readlines()
                graph_Coordinates_to_be.close()   
                
                os.mkdir("./AutoSavedResults/"+path+"/"+testName+io)
                data=open("./AutoSavedResults/"+path+"/"+testName+io+"/graph_Coordinates", "w+")
                for line in results:
                    data.write(line)
                data.close()
                
                testParam=open("./AutoSavedResults/"+path+"/"+testName+io+"/testParameters", "w+")
                testParam.write(section)
                testParam.write(directoryNames[directoryNameIndex])
                testParam.write('\n')
                hardware=open("./BenchMKresults/hardware", "r+")
                lines=[]
                for line in hardware:
                    lines.append(line)
                hardware.close()    
                lines = [line for line in lines[1:(len(line)-1)]]
                for line in lines:
                    testParam.write(line)
                testParam.close()
                
                y_axis = []
                x_axis = []
                ALLtheData=[]
                IOPS_y_axis=[] 
                BW_y_axis=[]   
                
                for line in results:
                    throughput = re.search("(\d+),(\d+\.*\d*),(\d+\.*\d*)", line)
                    if throughput != None:
                        print(throughput)
                        if throughput.group(1) not in x_axis:
                            x_axis.append(throughput.group(1))
                            ALLtheData.append([throughput.group(1), throughput.group(2), throughput.group(3)]) 
    
                for dataPoint in ALLtheData:
                    BW=float(dataPoint[2])
                    IOPS=float(dataPoint[1])
                    IOPS_y_axis.append(IOPS)
                    BW_y_axis.append(BW)     
                print(IOPS_y_axis)
                print(BW_y_axis)
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
                plt.savefig("./AutoSavedResults/"+path+"/"+testName+io+"/graphs.png")

dest = os.path.join("./BenchMKresultsArchive", path)

shutil.copytree("./BenchMKresults", dest)





