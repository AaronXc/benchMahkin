#!/bin/usr/env python3
import subprocess
import re 
import os
import sys
import json
from benchMKscriptVars import noAlternating, alternatingPorts, alternatingPortsAndCards, alternatingCards, directoryNames, globalSection, globalSection2, globalSection3,\
 globalSections, driveOrders
#open json file containing all the results and write it into a csv
#get the fio parameters for each section of the csv
#save in the hardware named directory
# this should be part of GraphPerformance, really

def organizeData(lines): 
                         
    # if the keys need to be changed in this dict, change the names written into the hardware file in BenchMKresults using createBenchMKresults
    # there are some keys that will not work because the GraphPerformance looks for them to change them in BenchMKresults/hardware: [global], directoryName (as in benchMKscriptVars)                     
    # and the name that group_reporting is changed to will have to be changed in GraphPerformance as well, in the part of the program that writes the testParameters
    
    order_of_data={
        "filesize": None,
        "bs": None,
        "ioengine": None,
        "readwrite": None,
        "iodepth": None,
        "direct": None,
        "numjobs": None,
        "group_reporting": None,
        "filename": None,
        "Motherboard_Model": None,
        "CPU_Type": None,
        "CPU_qty": None,
        "cores": None,
        "threads": None,
        "RAM_(GB)": None,
        "HBA_Card_1": None,
        "Model1": None,
        "slot1": None,
        "Bus Address1": None,
        "HBA_Card_2": None,
        "Model2": None,
        "slot2": None,
        "Bus Address2": None
    }  
    tagOrder=order_of_data.keys()    
    for line in lines:
        line = line.strip()
        tag = re.search("(.+),.+", line)
        if tag != None and tag.group(1) in tagOrder:
            order_of_data[tag]=line
        elif tag == None:
            hbacard=re.search("(HBA.+)", line)
            if hbacard != None:
                order_of_data[hbacard]=line
    new_lines=[]
    for tag in tagOrder:
        new_lines.append(order_of_data[tag])
    print(new_lines)
    return new_lines

path=input("hardwareName: \n>> ")
if os.path.exists("./"+path+"/allResults.json"):
    f=open("./"+path+"/allResults.json")
    allData=json.load(f)
    f.close()
    f=open("libreOfficeData", "w+")
    for directoryName in directoryNames:
    
        readBW=allData[directoryName]["reads"]["bw"].keys()
        
        readIOPS=allData[directoryName]["reads"]["iops"].keys() 
        
        writeBW=allData[directoryName]["writes"]["bw"].keys()
        
        writeIOPS=allData[directoryName]["writes"]["iops"].keys()        
        
        iotype=["reads","writes"]
        
        if os.path.exists("./"+path+"/BenchMKresults_"+directoryName+"/reads"+"/testParameters") and os.path.exists("./"+path+"/BenchMKresults_"+directoryName+"/writes"+"/testParameters"):
            for io in iotype:
                f.write(directoryName+"_"+io+"\n")
                if io == "reads":
                    f2=open("./"+path+"/BenchMKresults_"+directoryName+"/"+io+"/testParameters")
                    lines=f2.readlines()
                    f2.close()
                    lines=organizeData(lines)
                    for line in lines:
                        f.write(line+"\n")
                    if len(readBW) != 0:
                        f.write("readBW \n")
                        for key in readBW:
                            a=str(key)
                            b=str(allData[directoryName]["reads"]["bw"][key])                
                            f.write(a+","+b+"\n")
                    if len(readIOPS) != 0:
                        f.write("readIOPS \n")
                        for key in readIOPS: 
                            a=str(key)
                            b=str(allData[directoryName]["reads"]["iops"][key])
                            f.write(a+","+b+"\n")
                elif io == "writes":
                    f2=open("./"+path+"/BenchMKresults_"+directoryName+"/"+io+"/testParameters")
                    lines=f2.readlines()
                    f2.close()
                    lines=organizeData(lines)
                    for line in lines:
                        f.write(line+"\n")
                    if len(writeBW) != 0:
                        f.write("writeBW \n")
                        for key in writeBW:
                            a=str(key)
                            b=str(allData[directoryName]["writes"]["bw"][key])
                            f.write(a+","+b+"\n")
                    if len(writeIOPS) != 0:
                        f.write("writeIOPS \n")
                        for key in writeIOPS:
                            a=str(key)
                            b=str(allData[directoryName]["writes"]["iops"][key])
                            f.write(a+","+b+"\n")              
        else:
            for io in iotype:
                if os.path.exists("./"+path+"/BenchMKresults_"+directoryName+"/"+io+"/testParameters"):
                    f.write(directoryName+"\n")
                    f2=open("./"+path+"/BenchMKresults_"+directoryName+"/"+io+"/testParameters")
                    lines=f2.readlines()
                    f2.close()
                    lines=organizeData(lines)
                    for line in lines:
                        f.write(line+"\n")
                    if len(readBW) != 0:
                        f.write("readBW \n")
                        for key in readBW:
                            a=str(key)
                            b=str(allData[directoryName]["reads"]["bw"][key])                
                            f.write(a+","+b+"\n")
                    if len(readIOPS) != 0:
                        f.write("readIOPS \n")
                        for key in readIOPS: 
                            a=str(key)
                            b=str(allData[directoryName]["reads"]["iops"][key])
                            f.write(a+","+b+"\n")
                    if len(writeBW) != 0:
                        f.write("writeBW \n")
                        for key in writeBW:
                            a=str(key)
                            b=str(allData[directoryName]["writes"]["bw"][key])
                            f.write(a+","+b+"\n")
                    if len(writeIOPS) != 0:
                        f.write("writeIOPS \n")
                        for key in writeIOPS:
                            a=str(key)
                            b=str(allData[directoryName]["writes"]["iops"][key])
                            f.write(a+","+b+"\n")
    f.close()                    
    #noAlternating, alternatingPorts, alternatingPortsAndCards, alternatingCards, 
    if os.path.exists("./drivePatterns"):
        pass
    else:
        os.mkdir("./drivePatterns")
    f=open("./drivePatterns/noAlternating", "w+")
    f.write("noAlternating\n")
    for drive in noAlternating:
        alias=re.search("/dev/(.*)", drive)
        f.write(alias.group(1)+"\n")
    f.close()
    
    f=open("./drivePatterns/alternatingCards", "w+")
    f.write("alternatingCards\n")
    for drive in alternatingCards:
        alias=re.search("/dev/(.*)", drive)
        f.write(alias.group(1)+"\n")
    f.close()        
        
    f=open("./drivePatterns/alternatingPorts", "w+")
    f.write("alternatingPorts\n")
    for drive in alternatingPorts:
        alias=re.search("/dev/(.*)", drive)
        f.write(alias.group(1)+"\n")
    f.close()
        
    f=open("./drivePatterns/alternatingPortsAndCards", "w+")
    f.write("alternatingPortsAndCards\n")
    for drive in alternatingPortsAndCards:
        alias=re.search("/dev/(.*)", drive)
        f.write(alias.group(1)+"\n")
    f.close()
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        