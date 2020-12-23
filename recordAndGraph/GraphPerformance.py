import subprocess
import re
import os
import matplotlib.pyplot as plt
import  numpy as np
import shutil
import json
from benchMKscriptVars import noAlternating, alternatingPorts, alternatingPortsAndCards, alternatingCards, directoryNames, globalSection, globalSection2, \
    globalSection3, globalSections, driveOrders, sectionToNameMap, orderToNameMap, order_of_HBA1Params, order_of_HBA2Params, order_of_fioParams, order_of_serverParams

######################################################################################################################################################################################
# Part 1:
#   Create the directories to contain the results from the benchMKresults directory. 
#   Create a directory named AutoSavedResults that will contain directories for each different hardware setup tested on the serverOrder.
#   Use the string on the first line in the file in benchMKresults named "hardware" to name the directory for the hardware setup that was tested most recently.
#   Create a sub-directory of the "hardware setup directory" for each test run using a distinct drive order and a distinct i/o type.
#   Create sub-directories in each test's directory for results from reads and results from writes.
#   Write a file containing coordinates in csv format that can be graphed. Write a file containing all of the parameters for the test (hardware on the motherboard, parameters of
#   the fio test, and the drive order. Graph the results using the matplotlib module.
#   Save a json version of the results.
######################################################################################################################################################################################
ioType = ["/reads", "/writes"]

hardware=open("./BenchMKresults/hardware", "r+")
path=hardware.readline()  
path=path.strip()                                    # path is the sub-directory in AutoSavedResults where the results for this batch of results from BenchMKresults will be saved
hardware.close()

if os.path.exists("./AutoSavedResults") == False:
    os.mkdir("./AutoSavedResults")
if os.path.exists("./AutoSavedResults/"+path) == False:
    os.mkdir("./AutoSavedResults/"+path)

resultsJS=open("./BenchMKresults/allResults.json", "r+") # save the json version of the data in allResults.json
jsonData=resultsJS.readlines()
resultsJS.close()

resultsJS=open("./AutoSavedResults/"+path+"/allResults.json", "w+")
for line in jsonData:
    resultsJS.write(line)
resultsJS.close()

for directoryName in directoryNames:
    
    testName="BenchMKresults_"+directoryName
    os.mkdir("./AutoSavedResults/"+path+"/"+testName)
    
    for io in ioType:
        if os.path.exists("BenchMKresults/"+testName+io):
            graph_Coordinates_to_be=open("BenchMKresults/"+testName+io, "r") 
            results = graph_Coordinates_to_be.readlines()                           # get the data from BenchMKresults
            graph_Coordinates_to_be.close()   
            
            os.mkdir("./AutoSavedResults/"+path+"/"+testName+io)                                    
            data=open("./AutoSavedResults/"+path+"/"+testName+io+"/graph_Coordinates", "w+")
            for line in results:                                                                    
                data.write(line)
            data.close()                                                            # write the data from BenchMKresults
            
            testParam=open("./AutoSavedResults/"+path+"/"+testName+io+"/testParameters", "w+")
            fioGlobalSection=sectionToNameMap[directoryName].split("\n")
            for line in fioGlobalSection:
                fioGlobalSection[fioGlobalSection.index(line)]=fioGlobalSection[fioGlobalSection.index(line)].strip()
            lines=[]  
            hardware=open("./BenchMKresults/hardware", "r+")
            for component in hardware:
                lines.append(component)
            hardware.close()
            lines.append(directoryName)                                         # get and write the test paramters
            
            #############get rid of the first 2 lines of the fio globalSection for the test parameters files##############################################
            
            fioParam=fioGlobalSection[2:len(fioGlobalSection)]
            lines+=fioParam
            lines.append(("filename="+orderToNameMap[directoryName]+"\n"))

            for line in lines:
                line=line.strip()
                line=line.replace("=", ",")
                if line == "group_reporting":
                    testParam.write("group_reporting,yes")
                else:
                    testParam.write(line+"\n")
            testParam.close()
    
            ############ graph the results using matplotlib ##################################################################################################
    
            y_axis = []
            x_axis = []
            ALLtheData=[]
            IOPS_y_axis=[] 
            BW_y_axis=[]   
            
            for line in results:
                throughput = re.search("(\d+),(\d+\.*\d*),(\d+\.*\d*)", line)
                if throughput != None:
                    if throughput.group(1) not in x_axis:
                        x_axis.append(throughput.group(1))
                        ALLtheData.append([throughput.group(1), throughput.group(2), throughput.group(3)]) 
    
            for dataPoint in ALLtheData:
                BW=float(dataPoint[2])
                IOPS=float(dataPoint[1])
                IOPS_y_axis.append(IOPS)
                BW_y_axis.append(BW)     
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

        ############################ back-up past benchMKresults to a directory named BenchMKresultsArchive ###########################################

dest = os.path.join("./BenchMKresultsArchive", path)

shutil.copytree("./BenchMKresults", dest)



######################################################################################################################################################################################
# Part 2:
#   open json file containing all the results and write it into a csv
#   get the fio parameters for each section of the csv
#   save in the hardware named directory
#   
#
######################################################################################################################################################################################

######################################################################################################################################################################################
# organizeData:
#   args: lines (the lines of information about the test from the testParameters file for the given test)
#   desc: organize the lines into groupings that match the tables that are in the LibreOffice template so the data can easily be copied and pasted in
#   returns: sorted, formatted data
######################################################################################################################################################################################

def organizeData(lines): 
    
    #    
    # if the keys need to be changed in this dict, change the names written into the hardware file in BenchMKresults using createBenchMKresults
    # there are some keys that will not work because the GraphPerformance looks for them to change them in BenchMKresults/hardware: [global], directoryName (as in benchMKscriptVars)                     
    # and the name that group_reporting is changed to will have to be changed in GraphPerformance as well, in the part of the program that writes the testParameters
    
    fioOrder=order_of_fioParams.keys() 
    serverOrder=order_of_serverParams.keys()
    HBA1Order=order_of_HBA1Params.keys()
    HBA2Order=order_of_HBA2Params.keys()
    

    for line in lines:
        line = line.strip()
        tag = re.search("(.+),.+", line)
        if tag != None and tag.group(1) in fioOrder:
            order_of_fioParams[tag.group(1)]=line
        elif tag != None and tag.group(1) in HBA1Order:
            order_of_HBA1Params[tag.group(1)]=line
        elif tag != None and tag.group(1) in HBA2Order:
            order_of_HBA2Params[tag.group(1)]=line
        elif tag != None and tag.group(1) in serverOrder:
            order_of_serverParams[tag.group(1)]=line
            
    new_lines=[]
    for tag in fioOrder:
        new_lines.append(order_of_fioParams[tag]+"\n")
    new_lines.append("\n")
    for tag in serverOrder:
        new_lines.append(order_of_serverParams[tag]+"\n")
    new_lines.append("\n")
    for tag in HBA1Order:
        new_lines.append(order_of_HBA1Params[tag]+"\n")
    new_lines.append("\n")
    for tag in HBA2Order:
        new_lines.append(order_of_HBA2Params[tag]+"\n")
    new_lines.append("\n")
    return new_lines

if os.path.exists("./AutoSavedResults/"+path+"/allResults.json"):
    f=open("./AutoSavedResults/"+path+"/allResults.json")
    allData=json.load(f)
    f.close()
    f=open("./AutoSavedResults/"+path+"/resultsForLOCalc", "w+")
    for directoryName in directoryNames:
    
        readBW=allData[directoryName]["reads"]["bw"].keys()
        
        readIOPS=allData[directoryName]["reads"]["iops"].keys() 
        
        writeBW=allData[directoryName]["writes"]["bw"].keys()
        
        writeIOPS=allData[directoryName]["writes"]["iops"].keys()        
        
        iotype=["reads","writes"]
        
        if os.path.exists("./AutoSavedResults/"+path+"/BenchMKresults_"+directoryName+"/reads"+"/testParameters") and os.path.exists("./AutoSavedResults/"+path+"/BenchMKresults_"+directoryName+"/writes"+"/testParameters"):
            for io in iotype:
                f.write(directoryName+"_"+io+"\n(sheet name)\n\n")
                if io == "reads":
                    f2=open("./AutoSavedResults/"+path+"/BenchMKresults_"+directoryName+"/"+io+"/testParameters")
                    lines=f2.readlines()
                    f2.close()
                    lines=organizeData(lines)
                    for line in lines:
                        f.write(line)
                    if len(readBW) != 0:
                        f.write("readBW \n")
                        for key in readBW:
                            a=str(key)
                            b=str(allData[directoryName]["reads"]["bw"][key])                
                            f.write(a+","+b+"\n")
                        f.write("\n") 
                    if len(readIOPS) != 0:
                        f.write("readIOPS \n")
                        for key in readIOPS: 
                            a=str(key)
                            b=str(allData[directoryName]["reads"]["iops"][key])
                            f.write(a+","+b+"\n")
                        f.write("\n")
                elif io == "writes":
                    f2=open("./AutoSavedResults/"+path+"/BenchMKresults_"+directoryName+"/"+io+"/testParameters")
                    lines=f2.readlines()
                    f2.close()
                    lines=organizeData(lines)
                    for line in lines:
                        f.write(line)
                    if len(writeBW) != 0:
                        f.write("writeBW \n")
                        for key in writeBW:
                            a=str(key)
                            b=str(allData[directoryName]["writes"]["bw"][key])
                            f.write(a+","+b+"\n")
                        f.write("\n") 
                    if len(writeIOPS) != 0:
                        f.write("writeIOPS \n")
                        for key in writeIOPS:
                            a=str(key)
                            b=str(allData[directoryName]["writes"]["iops"][key])
                            f.write(a+","+b+"\n")
                        f.write("\n")        
        else:
            for io in iotype:
                if os.path.exists("./AutoSavedResults/"+path+"/BenchMKresults_"+directoryName+"/"+io+"/testParameters"):
                    f.write(directoryName+"\n(sheet name)\n\n")
                    f2=open("./AutoSavedResults/"+path+"/BenchMKresults_"+directoryName+"/"+io+"/testParameters")
                    lines=f2.readlines()
                    f2.close()
                    lines=organizeData(lines)
                    for line in lines:
                        f.write(line) 
                    if len(readBW) != 0:
                        f.write("readBW \n")
                        for key in readBW:
                            a=str(key)
                            b=str(allData[directoryName]["reads"]["bw"][key])                
                            f.write(a+","+b+"\n")
                        f.write("\n") 
                    if len(readIOPS) != 0:
                        f.write("readIOPS \n")
                        for key in readIOPS: 
                            a=str(key)
                            b=str(allData[directoryName]["reads"]["iops"][key])
                            f.write(a+","+b+"\n")
                        f.write("\n") 
                    if len(writeBW) != 0:
                        f.write("writeBW \n")
                        for key in writeBW:
                            a=str(key)
                            b=str(allData[directoryName]["writes"]["bw"][key])
                            f.write(a+","+b+"\n")
                        f.write("\n") 
                    if len(writeIOPS) != 0:
                        f.write("writeIOPS \n")
                        for key in writeIOPS:
                            a=str(key)
                            b=str(allData[directoryName]["writes"]["iops"][key])
                            f.write(a+","+b+"\n")
                        f.write("\n") 
    f.close()
    #noAlternating, alternatingPorts, alternatingPortsAndCards, alternatingCards, 
    
    f=open("./AutoSavedResults/"+path+"/driveOrdersForLOCalc", "w+")
    f.write("noAlternating\n")
    for drive in noAlternating:
        alias=re.search("/dev/(.*)", drive)
        f.write(alias.group(1)+"\n")
    f.write("\n") 

    f.write("alternatingCards\n")
    for drive in alternatingCards:
        alias=re.search("/dev/(.*)", drive)
        f.write(alias.group(1)+"\n")
    f.write("\n")         

    f.write("alternatingPorts\n")
    for drive in alternatingPorts:
        alias=re.search("/dev/(.*)", drive)
        f.write(alias.group(1)+"\n")
    f.write("\n") 

    f.write("alternatingPortsAndCards\n")
    for drive in alternatingPortsAndCards:
        alias=re.search("/dev/(.*)", drive)
        f.write(alias.group(1)+"\n")
    f.close()

    f=open("./AutoSavedResults/"+path+"/resultsForLOCalc", "r+")
    lines=f.readlines()
    f.close()
    formulas=[]
    linecount=0;
    graphableDATA = False
    graphableDATArange = []
    for line in lines:
        linecount+=1
        parameterValue = re.search("^.+,.+$", line)
        readBW = re.search("readBW", line)
        writeBW = re.search("writeBW", line)
        readIOPS = re.search("readIOPS", line)
        writeIOPS = re.search("writeIOPS", line)
        if readBW != None or writeBW != None or readIOPS != None or writeIOPS != None and graphableDATA == False:            
            graphableDATA = True
            graphableDATArange.append([linecount+1,None])
            
        elif graphableDATA == True:
            print(linecount)
            graphableDATArange[len(graphableDATArange)-1][1] = linecount
            if line == "\n":
                graphableDATA = False    
                print("left gettingRange state")
                formulas.append("$results.$B${begin}:$B${end}\n".format(begin=graphableDATArange[len(graphableDATArange)-1][0], end=graphableDATArange[len(graphableDATArange)-1][1]))
        elif parameterValue and line != "\n":
            formulas.append("=$results.$B${lc}\n".format(lc=linecount))
        if not parameterValue and line != "\n":
            formulas.append("=$results.$A${lc}\n".format(lc=linecount))
        if line == "\n":
            formulas.append(line)
    f=open("./AutoSavedResults/"+path+"/formulasLOCalcResults", "w+")
    for formula in formulas:
        f.write(formula)
    f.close()
    
    f=open("./AutoSavedResults/"+path+"/driveOrdersForLOCalc", "r+")
    formulas=[]
    linecount=0;
    for line in f:
        linecount+=1
        if line != "\n":
            formulas.append("=$driveOrders.$A${lc}\n".format(lc=linecount))
        if line == "\n":
            formulas.append(line)
    f=open("./AutoSavedResults/"+path+"/formulasLOCalcDriveOrders", "w+")
    for formula in formulas:
        f.write(formula)
    f.close()